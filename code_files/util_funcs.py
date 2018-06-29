from collections import defaultdict
import csv
import pickle

from gensim.models import KeyedVectors
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer

########################################################################
########################### Data Processing ############################
########################################################################
def remove_low_freq_words(corpus, freq_thresh=10):
    # Store frequency of each Word
    from collections import defaultdict
    frequency = defaultdict(int)
    for doc in corpus:
        for token in doc:
            frequency[token] += 1

    # Filter titles
    new_corpus = []
    for doc in corpus:
        filtered_doc = [w.lower() for w in doc if frequency[w] > freq_thresh]
        new_corpus.append(filtered_doc)

    new_corpus = [doc for doc in new_corpus if doc]  # Removes empty lists
    return new_corpus

def to_sentences(texts):
    text_sentences = []
    for text in texts:
        text_sentences = text_sentences + sent_tokenize(text)
    print('# sentences: ',len(text_sentences))

def save_corpus_pickle(path, corpus):
    with open(path, 'wb') as f:
        pickle.dump(corpus, f)
        print('corpus saved.')

def load_corpus_pickle(path): 
    with open(path, 'rb') as f:
        corpus = pickle.load(f)
        print('corpus loaded.')
        return corpus

def save_corpus_csv(path, corpus):
    # Save cleaned corpus
    with open(path, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(corpus)
        print('corpus saved.')

def load_corpus_csv(path):
    """
    Loads saved csv-format corpus at path.

    Output:
        corpus: list of documents.
    """

    with open(path, "r") as f:
        reader = csv.reader(f)
        corpus = list(reader)
    return corpus


########################################################################
########################### Corpus Functions ###########################
########################################################################
def count_frequency(docs, tokenized=True):
    frequency = defaultdict(int)
    tokenizer = RegexpTokenizer(r'\w+')
    for doc in docs:
        if not tokenized:
            doc = tokenizer.tokenize(doc)
        for token in doc:
            frequency[token] += 1
    return frequency

def search(corpus, tokenized=True, words=[], verbose=False, max_count=None):
    """
    Searches corpus for the words in "words". Returns dictionary containing
    document numbers where each word appears.
    """
    def print_found(): 
        for k, v in locations.items():
            print('found {} occurences of {}'.format(len(v), k))
    
    locations = defaultdict(list)
    tokenizer = RegexpTokenizer(r'\w+')
    for i, doc in enumerate(corpus):
        if not tokenized:
            doc = tokenizer.tokenize(doc)
        for token in doc:
            if token in words:
                locations[token].append(i)
                if max_count and len(locations[token]) >= max_count:
                    if verbose:
                        print_found()
                    return locations
                break 
    if verbose:
        print_found()
                
    return locations

########################################################################
############################# Clustering ###############################
########################################################################
# Addiction. # Notes: Drug names go here?
addiction_seeds = set(['cravings', 'relapse', 'alcoholic', 'addict', 'dependent', 'addicted', 'addiction', 'help', 'advice'])

# Recovery / "Seekig Help"
recovery_seeds = set(['recovering', 'sober', 'therapy', 'support', 
                  'clean', 'rehab', 'aa', 'aa_meeting'])


seeds_dict = {#'pre_addiction': pre_addiction_seeds,
             'addiction': addiction_seeds,
             'recovery': recovery_seeds}

def get_addiction_seeds():
    return addiction_seeds

def get_recovery_seeds():
    return recovery_seeds

def get_cluster_members(kmeans, word):
    cluster_labels = kmeans.labels_
    idx = np.argwhere(np.array(words) == word)  # index of word
    k = cluster_labels[idx][0][0]  # cluster assignment of word
    members = np.argwhere(cluster_labels == k)  # all members of word's cluster
    return np.array(words)[members]


# Pre-Addiction
# pre_addiction_seeds = set(['nothing_wrong', 'moderation', 'try', 'tried', 'trying', 'start'])

# Addiction. # Notes: Drug names go here?
addiction_seeds = set(['cravings', 'relapse', 'alcoholic', 'addict', 'dependent', 'addicted', 'addiction', 'help', 'advice'])

# Recovery / "Seekig Help"
recovery_seeds = set(['recovering', 'sober', 'therapy', 'support', 
                  'clean', 'rehab', 'aa', 'aa_meeting'])


seeds_dict = {#'pre_addiction': pre_addiction_seeds,
             'addiction': addiction_seeds,
             'recovery': recovery_seeds}

def cluster_score(cluster_model, gensim_model, n_clusters, labels=None):
    # Psuedo-code:
    # Compare each cluster to each seed list
    #    - if cluster has no seed, score is 0 for that cluster
    #    - otherwise, calculate similarity between cluster and each
    #      seed list represented.
    
    """
        Inputs:
            cluster_model: e.g. kmeans, agglomerative, gaussian mix...
            gensim_model: gensim_model
            n_clusters: number of clusters in cluster_model
            labels: cluster assignments (optional).
        
        Outputs:
            final_score: cluster model score
    """
    
    final_score = 0.0
    words_arr = np.array(list(gensim_model.wv.vocab))
    word_vectors = gensim_model[gensim_model.wv.vocab]
    if labels is None:
        if hasattr(cluster_model, 'labels_'):
            labels = cluster_model.labels_
        else:
            labels = cluster_model.predict(word_vectors)
    for i in range(n_clusters): 
        # Get members in cluster i
        member_indicies = np.argwhere(labels == i)
        member_words = words_arr[member_indicies].flatten()
        aspects_found = 0
        similarity = 0.
        for k, seeds in seeds_dict.items():
            if (set(seeds) & set(member_words)):
                aspects_found += 1
                similarity += gensim_model.wv.n_similarity(seeds, member_words)
        # Take average
        if aspects_found > 0: similarity /= aspects_found
        final_score += similarity
                      
    return final_score
        
    
def find_best_k(cluster_model_type, gensim_model, k_values, print_every=10):
    
    """
        Inputs:
            cluster_model_type: {'agg', 'gm' (gaussian mixture), 'kmeans'}
            gensim_model: gensim_model
            k_values: an iterable containing values of n_clusters
        
        Outputs:
            scores: list of scores corresponding to each k_value
    """
    
    scores = []
    word_vectors = gensim_model[gensim_model.wv.vocab]
    
    it = 0
    for k in k_values:
        cluster_model = None
        if cluster_model_type == 'agg':
            cluster_model = AgglomerativeClustering(n_clusters=k)
        elif cluster_model_type == 'gm':
            cluster_model = GaussianMixture(n_components=k)
        elif cluster_model_type == 'kmeans':
            cluster_model = KMeans(n_clusters=k)
        else:
            raise Exception('invalid cluster_model_type')
        
        cluster_model.fit(word_vectors)
        score = cluster_score(cluster_model, gensim_model, n_clusters=k)
        scores.append(score)
        
        if it % print_every == 0:
            print('Finisehd {} clusters, score: {}'.format(k, score))
        it += 1
        
    return scores


def assign_clusters(cluster_model, gensim_model, labels=None, n_clusters=None):
    """
        Inputs:
            cluster_model: e.g. kmeans, agglomerative, gaussian mix...
            gensim_model: gensim_model
            labels: cluster assignments.
            n_clusters: number of clusters in cluster_model
        
        Outputs:
            cluster_groups: Dictionary containing with format {'group_name' : clusters}
                            where 'group_name' is a string indicating the group (e.g. 'addiction')
                            and 'clusters' is a list of clusters (numbers) assigned to the group.
                            
            similarities_dict: Stores similarity scores between each cluster and each seed list. 
                               Lists are ordered by cluster number. E.g. similarities_dict['addiction'][i]
                               is the similarity score between cluster i and addiction seed_list
    """
    
    cluster_groups = {#'pre_addiction': pre_addiction_clusters,
                 'addiction': [],
                 'recovery': []}

    similarities_dict = {# 'pre_addiction': [],
                 'addiction': [],
                 'recovery': []}
    
    words_arr = np.array(list(gensim_model.wv.vocab))
    word_vectors = gensim_model[gensim_model.wv.vocab]
    if n_clusters is None:
        n_clusters = cluster_model.n_clusters
    
    if labels is None:
        if hasattr(cluster_model, 'labels_'):
            labels = cluster_model.labels_
        else:
            labels = cluster_model.predict(word_vectors)
    
    for i in range(n_clusters):
        # Get members of cluster i
        member_indicies = np.argwhere(labels == i)
        member_words = words_arr[member_indicies].flatten()

        # Find the group that cluster i is most similar to based on group seeds
        max_sim = -1.
        most_sim_group = None
        for k, cluster_group in cluster_groups.items():
            group_seeds = seeds_dict[k]
            sim = gensim_model.wv.n_similarity(group_seeds, member_words)
            similarities_dict[k].append(sim)
            if sim > max_sim:
                max_sim = sim
                most_sim_group = k

        # Add cluster to a group
        cluster_groups[most_sim_group].append(i)
        
    return cluster_groups, similarities_dict


def cluster_table(group_name, cluster_model, gensim_model, top_n=10, max_words_per_cluster=4, labels=None, n_clusters=None):
    """
        Inputs:
            group_name: name of group. (e.g. 'addiction', 'recovery',...)
            cluster_model: e.g. kmeans, agglomerative, gaussian mix...
            gensim_model: gensim_model
            top_n: the top n clusters will appear in the table.
            labels: cluster assignments.
            n_clusters: number of clusters in cluster_model
        
        Outputs:
            A Dataframe with the top_n clusters and there corresponding top words
                            
    """
    
    words_arr = np.array(list(gensim_model.wv.vocab))
    word_vectors = gensim_model[gensim_model.wv.vocab]
    if labels is None:
        if hasattr(cluster_model, 'labels_'):
            labels = cluster_model.labels_
        else:
            labels = cluster_model.predict(word_vectors)
    
    cluster_groups, similarities_dict = assign_clusters(cluster_model, gensim_model, labels=labels, n_clusters=n_clusters)
    top_n_clusters = np.array(similarities_dict[group_name]).argsort()[::-1][:top_n]
    
    # top words for each top n cluster
    top_clusters = {'cluster #': top_n_clusters, 'top words': []}
    for c in top_n_clusters:
        word_sims = [] # To find top words for cluster c. Top words is based on similarty to seed list  
        words_in_cluster = words_arr[np.argwhere(labels == c)]
        for word in words_in_cluster:
            word_sims.append(gensim_model.n_similarity(seeds_dict[group_name], word))
        
        # Extract Top Words in Cluster c
        top_words_idx = sorted(range(len(word_sims)), key=lambda i: word_sims[i])[-max_words_per_cluster:]
        top_words = np.array(words_in_cluster).flatten()[top_words_idx]
        top_clusters['top words'].append(top_words)
        
    return pd.DataFrame(top_clusters)