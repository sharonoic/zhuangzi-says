from seed.seed_quotes import sample_quotes
from utils.logic import tag_map

alltags = []

for quote in sample_quotes:
    alltags.extend(quote["tags"])

tags_from_answers = set()
for tag_list in tag_map.values():
    tags_from_answers.update(tag_list)

missing_tags = tags_from_answers - set(alltags)

print(missing_tags)
