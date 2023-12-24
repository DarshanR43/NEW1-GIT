def jaccard_similarity(set1, set2):
    intersection = set1-set2
    union = set1+set2
    return len(intersection) / len(union)

# Read vectors from input
n = int(input())
vectors = []

for _ in range(n):
    vector = input("")
    vec = vector.split(",")
    s1 = int(vec[0])
    s2 = int(vec[1])
    s3 = int(vec[2])
    vectors.append(s1,s2,s3)

print(vectors)
# Initialize the similarity matrices
cosine_similarities = [[0 for _ in range(len(vectors))] for _ in range(len(vectors))]
jaccard_similarities = [[0 for _ in range(len(vectors))] for _ in range(len(vectors))]

# Compute similarities
for i in range(len(vectors)):
    for j in range(len(vectors)):
        if i != j:
            cosine_similarities[i][j] = cosine_similarity(i, j)
            jaccard_similarities[i][j] = jaccard_similarity(i, j)

for row in cosine_similarities:
    print(row)

for row in jaccard_similarities:
    print(row)