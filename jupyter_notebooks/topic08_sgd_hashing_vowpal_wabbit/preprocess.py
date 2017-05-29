import sys

from tqdm import tqdm


tags = ['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']
tags_set = set(tags)


def preprocess():
    args = sys.argv[1:]
    file_in = args[0]
    file_out = args[1]

    lines_selected = 0
    lines_corrupted = 0

    with open(file_in, 'r') as fin:
        with open(file_out, 'w') as fout:
            for line in tqdm(fin):

                line = line.strip()

                if line.count('\t') != 1:
                    lines_corrupted += 1
                    continue

                text, line_tags = line.split('\t')
                text = text.replace(":", "").replace("|", "")
                line_tags = set(map(lambda s: s.lower(), line_tags.split(' ')))

                if not text:
                    lines_corrupted += 1
                    continue

                if len(line_tags & tags_set) == 1:
                    label = list(line_tags & tags_set)[0]
                    label_id = tags.index(label) + 1
                    fout.write("%d | %s\n" % (label_id, text))
                    lines_selected += 1

    print("%d lines selected, %d lines corrupted." % (lines_selected, lines_corrupted))

# Expected:
# 10000000it [01:20, 123690.31it/s]
# 4389054 lines selected, 15 lines corrupted.

if __name__ == "__main__":
    preprocess()