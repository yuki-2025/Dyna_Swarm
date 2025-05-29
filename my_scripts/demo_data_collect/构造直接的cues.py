

from my_scripts.io_utils import load_json, dump_json, dump_jsonl

list_samples = load_json(
    "datasets/crosswords/train.json"
)

list_direct_demos = []
for samp in list_samples:
    print(samp)

    letters = samp[1]
    cues = samp[0]

    h1 = "".join(letters[0: 5]).lower()
    h2 = "".join(letters[5: 10]).lower()
    h3 = "".join(letters[10: 15]).lower()
    h4 = "".join(letters[15: 20]).lower()
    h5 = "".join(letters[20: 25]).lower()

    h1_cue = cues[0]
    h2_cue = cues[1]
    h3_cue = cues[2]
    h4_cue = cues[3]
    h5_cue = cues[4]

    vs = []
    for i in range(5):
        tmp_ = "".join([letters[0 + 1], letters[5 + 1], letters[10 + 1], letters[15 + 1], letters[20 + 1]]).lower()
        vs.append(tmp_)

    v1 = vs[0]
    v2 = vs[1]
    v3 = vs[2]
    v4 = vs[3]
    v5 = vs[4]

    v1_cue = cues[5]
    v2_cue = cues[6]
    v3_cue = cues[7]
    v4_cue = cues[8]
    v5_cue = cues[9]

    for word_, cue_ in zip(
        [h1, h2, h3, h4, h5, v1, v2, v3, v4, v5],
        [h1_cue, h2_cue, h3_cue, h4_cue, h5_cue, v1_cue, v2_cue, v3_cue, v4_cue, v5_cue],

    ):
        print(word_, cue_)

        list_direct_demos.append(
            {"input": f"{word_} -- {cue_}", }
        )

print(list_direct_demos)
dump_jsonl(
    list_direct_demos,
    "my_scripts/demo_data_collect/direct_demos.json",
)


