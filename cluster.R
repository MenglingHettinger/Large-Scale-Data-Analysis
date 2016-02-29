library(vegan)
data200 <- read.table("20city200_removebias.txt", header = F, sep ="\t")
dataf5 <- read.table("20cityfreq5_removebias.txt", header = F, sep ="\t")
dataf10 <- read.table("20cityfreq10_removebias.txt", header = F, sep ="\t")
dim(data200)
dim(dataf5)
dim(dataf10)

datamatrix200 <- as.matrix(data200)
datamatrix200 <- t(datamatrix200)
datamatrixf5 <- as.matrix(dataf5)
datamatrixf5 <- t(datamatrixf5)
datamatrixf10 <- as.matrix(dataf10)
datamatrixf10 <- t(datamatrixf10)


d200 <- vegdist(datamatrix200, method="jaccard")
df5 <- vegdist(datamatrixf5, method="jaccard")
df10 <- vegdist(datamatrixf10, method="jaccard")

kmeansfit200 <- kmeans(d200, 4, iter.max = 10)
kmeansfitf5 <- kmeans(df5, 4, iter.max = 10)
kmeansfitf10 <- kmeans(df10, 4, iter.max = 10)

hclustfitcomp200 <- hclust(d200, method = "complete")
hclustfitsing200 <- hclust(d200, method = "single")

hclustfitcompf5 <- hclust(df5, method = "complete")
hclustfitsingf5 <- hclust(df5, method = "single")

hclustfitcompf10 <- hclust(df10, method = "complete")
hclustfitsingf10 <- hclust(df10, method = "single")



kmeans_k <- function(d){
	for(i in c(1:20)){
	kmeansfit <- kmeans(d, i, iter.max= 20)
	print(i)
	print(kmeansfit)	
	}
}





