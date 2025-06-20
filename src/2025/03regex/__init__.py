import re

pattern = r'^(?!.*(?:([2-9]\d*(?:\.\d+)?)x|x([2-9]\d*(?:\.\d+)?|1\.(?!0+$)\d+))).*$'
test_strings = ["🇸🇬 [开发测试]0.2x|GloB￫新加坡A", "🇮🇳 1.0x|GX5G集群￫印度", "🇭🇰 [新]2.0x|电信测试￫香港", "x1.0", "0.6x",
                "0.5x", "2.5x", "2.5x", "5.0x", "10.0x", "10x", "0.2x", "0.5",
                "🇭🇰 [新][企业专线CM]10x￫香港", "5x", "🇬🇧英国高级-1 x5", "🇺🇸美国高级 x5"]

max_length = max(len(s) for s in test_strings)

for string in test_strings:
    if re.match(pattern, string):
        print(f"{string:<{max_length}}    能 被正则表达式匹配")
    else:
        print(f"{string:<{max_length}}    不能 被正则表达式匹配")
