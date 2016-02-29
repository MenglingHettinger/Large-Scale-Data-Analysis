#!/usr/bin/env python

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer

def extract_hashtag(inPath,outPath):
    """ Reads in hashtag files and return only hashtag,  if "#" is the only char in the whole line, then the line is removed,
        unicodes are removed from the hashtag, all the letters are converted to lower case, 
    """ 

    print '\n[] Reading %s ...' % inPath
    outFile = open(outPath, 'w')
    with open(inPath, 'r') as inFile:
        for line in inFile:
            
            timestamp, hashtags = line.strip().split(":::")
            #print hashtags
            
            if hashtags == "#":
                continue
            
            hashtag_tup = hashtags.split("\\n")
            for hashtag in hashtag_tup:
                if "\u" in hashtag:
                    hashtag = hashtag.split("\u")[0]
            outFile.write("%s\n" % hashtag.lower()[1:])

        outFile.close()
        

def remove_noise(inPath, outPath):
    """ Remove the hashtags if they ONLY contain stopwords, punctuations or numbers.
        Remove stemEndings and punctuations at the end of each hashtag.
    """
    stopWords = [ "a", "i", "it", "am", "at", "on", "in", "to", "too", "very", \
                 "of", "from", "here", "even", "the", "but", "and", "is", "my", \
                 "them", "then", "this", "that", "than", "though", "so", "are" ]
    stemEndings = [ "s", "es", "ed", "er", "ly" "ing", "'s", "s'" ]
    punctuations = [ ".", ",", ":", ";", "!", "?","(",")","<",">","/","|","[","]","{","}"]
    numbers = ["0","1","2","3","4","5","6","7","8","9",]
    outFile = open(outPath, 'w')
    with open(inPath, 'r') as inFile:
        for line in inFile:
            line = line.strip()
            #print line
            
            if line in stopWords or line in punctuations or line in numbers:
                continue

            if line.isdigit():
                continue
            for ending in stemEndings:
                if line.endswith(ending):
                    #print line
                    line = line[:-len(ending)]
                    


            for punct in punctuations:
                if line.endswith(punct):
                    #print line
                    line = line[:len(punct)]
                    
            outFile.write("%s\n" % line)
    outFile.close()
    
def hashtag_to_list(inPath, outPath):
    """
    convert hashtags(each per line) into a list which contains all of the hashtags appears in one city
    """
    hashtag_list = []
    outFile = open(outPath,'w')
    with open(inPath, 'r') as inFile:
        for line in inFile:
            hashtag_list.append(line.strip()[1:])
    for item in hashtag_list:
        outFile.write("%s, " % item)
    outFile.close



def hashtag_to_string(inPath, outPath):
    """
    convert hashtags(each per line) into a list which contains all of the hashtags appears in one city
    """
    hashtag_string = ""
    outFile = open(outPath,'w')
    with open(inPath, 'r') as inFile:
        for line in inFile:
            hashtag_string += " "+line.strip()[1:]
   
        outFile.write("%s " % hashtag_string)
    outFile.close

def list_to_sparse(inPath_1,inPath_2,inPath_3, inPath_4, inPath_5, inPath_6, inPath_7, inPath_8, inPath_9,inPath_10, outPath):
    outFile = open(outPath,'w')
    hashlist_1 = open(inPath_1,'r')
    hashlist_2 = open(inPath_2,'r')
    hashlist_3 = open(inPath_3,'r')
    hashlist_4 = open(inPath_4,'r')
    hashlist_5 = open(inPath_5,'r')
    hashlist_6 = open(inPath_6,'r')
    hashlist_7 = open(inPath_7,'r')
    hashlist_8 = open(inPath_8,'r')
    hashlist_9 = open(inPath_9,'r')
    hashlist_10 = open(inPath_10,'r')
    hashlist = [hashlist_1,hashlist_2,hashlist_3,hashlist_4,hashlist_5,hashlist_6,hashlist_7,hashlist_8,hashlist_9,hashlist_10]
    vectorizer = CountVectorizer(min_df=1)
    hashsparse = vectorizer.fit_transform(hashlist)
    hashsparse.toarray() 
    print hashsparse
    print hashsparse.toarray()

def string_to_sparse(inPath_1,inPath_2,outPath):
    outFile = open(outPath,'w')
    with open(inPath_1,'r') as hashstring_1:
        data_1 = hashstring_1.read()
    with open(inPath_2,'r') as hashstring_2:
        data_2 = hashstring_2.read()
    #hashstring_2 = open(inPath_2,'r')
    #print hashstring_1
    hashstring = [data_1,data_2]
    #print hashstring
    vectorizer = CountVectorizer(min_df=1)
    hashsparse = vectorizer.fit_transform(hashstring = hashstring.astype(np.float))
    hashsparse = Normalizer(copy=False).fit_transform(hashsparse)
    return hashsparse

def sparse_to_cluster(sparse_matrix):
    km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1,
                verbose=opts.verbose)
    print("Clustering sparse data with %s" % km)
    t0 = time()
    km.fit(sparse_matrix)
    print("done in %0.3fs" % (time() - t0))
    print()

    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
    print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
    print("Adjusted Rand-Index: %.3f"
        % metrics.adjusted_rand_score(labels, km.labels_))
    print("Silhouette Coefficient: %0.3f"
        % metrics.silhouette_score(X, labels, sample_size=1000))

    print()




def remove_bias(inPath,outPath):
    """
    remove the words that only appear in one city or appear in all cities but one.
    """
    outFile = open(outPath, 'w')
    with open(inPath, 'r') as inFile:
        for line in inFile:
            cities_words = line.strip().split("\t")
            #for i in cities_words:
            #    i = int(i)
            num_zeros = cities_words.count("0")
            if num_zeros == 1 or num_zeros == 19:
                continue
            outFile.write("%s" % line)
    outFile.close()
    





def main():
    #extract_hashtag("hashtag_CHA.txt","extract_CHA.txt")
    #extract_hashtag("hashtag_DA.txt","extract_DA.txt")
    #remove_noise("extract_CHA.txt", "extract_CHA_clean.txt")
    #remove_noise("extract_DA.txt", "extract_DA_clean.txt")
    #hashtag_to_string("extract_CHA_clean.txt", "hashtagstring_CHA.txt")
    #hashtag_to_string("extract_DA_clean.txt", "hashtagstring_DA.txt")
    #hashtag_to_list("extract_CHI_lower.txt", "hashtaglist_CHI.txt")
    #string_to_sparse("hashtagstring_CHA.txt","hashtagstring_DA.txt","hashsparse.txt")
    #sparse_to_cluster(hashsparse)
    remove_bias("20city_freq5.txt","20cityfreq5_removebias.txt")
    remove_bias("20city_freq10.txt","20cityfreq10_removebias.txt")
    remove_bias("20city_200.txt","20city200_removebias.txt")
if __name__ == "__main__":
    main()

