import re

i_pronouns = ["i", "me", "i'm", "i've", "my"]
u_pronouns = ["you", "your", "u"]

help_seeds = ['any help', 'any advice', 'need help', 
        'need some help', 'want some help', 
        'want help', 'want advice', 'please help', 
        'need advice', 'need of help', 'help?', 
        'advice?', 'help me']

support_seeds = ['you got this', 'good luck', 'best of luck', 'feel better', 'can do it', 'can do this']
support_seeds_RE = re.compile(r'\b(%s)\b' % '|'.join(support_seeds), flags=re.IGNORECASE)

i_RE = re.compile(r'\b(%s)\b' % '|'.join(i_pronouns), flags=re.IGNORECASE)
u_RE = re.compile(r'\b(%s)\b' % '|'.join(u_pronouns), flags=re.IGNORECASE)
help_seeds_RE = re.compile(r'\b(%s)\b' % '|'.join(help_seeds), flags=re.IGNORECASE)

def get_help_labels(posts):
    pos_labels_idx = []
    for i, post in enumerate(posts):
        i_cts = 0
        u_cts = 0
        help_cts = 0
        for m in i_RE.finditer(post): 
            i_cts += 1
        for m in u_RE.finditer(post):
            u_cts += 1
        for m in help_seeds_RE.finditer(post):
            help_cts += 1
            
        # Criteria
        if help_cts > 2:      
            pos_labels_idx.append(i)
            continue
            
        if i_cts > u_cts and help_cts > 1 and post.count('?') > 1: 
            pos_labels_idx.append(i)
            continue
        
    return pos_labels_idx
        

def get_support_labels(comments):
    pos_labels_idx = []
    for i, comment in enumerate(comments):
        i_cts = 0
        u_cts = 0
        supp_cts = 0
        for m in i_RE.finditer(comment): 
            i_cts += 1
        for m in u_RE.finditer(comment):
            u_cts += 1
        for m in support_seeds_RE.finditer(comment):
            supp_cts += 1
            
        if supp_cts > 1: 
            pos_labels_idx.append(i)
            
    return pos_labels_idx

