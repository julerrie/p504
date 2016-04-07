class Trie(object):
    def __init__(self):
        self.children = {}
        self.flag = False # Flag to represent that a word ends at this node

    def add(self, char):
        self.children[char] = Trie()

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.add(char)
            node = node.children[char]
        node.flag = True

    def contains(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.flag

    def all_suffixes(self, prefix):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children: return results
        return reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return list(node.all_suffixes(prefix))

f = open('all_playlists.txt', 'r')
k = open('playlist_128.txt', 'w')
song = open('song_list.txt', 'r')
l = f.read().splitlines()
c = []
x = []
songlist1 = []
i = 0
playlist = {}
songlist = {}
songlist2 = {}
namelist=[]
tmp = ()
trie = Trie()
for item in l:
    key,value = item.split("\t")
    playlist[key]=int(value)
f.close()
for item in song:
    if item.__contains__('\n'):
        tmp = item[0:-1]
    else:
        tmp = item
    a = int(len(tmp))
    b = int(tmp.find('\t'))
    str1 = tmp[0:b]
    str2 = tmp[b + 1:a]
    key, value = str1, str2
    songlist[key] = value
song.close()
for y in songlist:
    tmp = songlist[y].split("\t")
    key, value = tmp[0], tmp[1]
    songlist2[key] = value
    trie.insert(key)
#name=raw_input()
songpop={}
allsongpop={}
for item in songlist2:
    songname=item
#        print songname
    for item in songlist:
        if songname in songlist[item]:
            songnamelist=" "+item+" "
            pop = -1
            for items1 in playlist:
                if songnamelist in items1:
                    pop=pop+playlist[items1]
            if pop == -1:
                break
            else:
                pop=pop+1
                songpop[songname]=pop
                allsongpop.update(songpop)
                break
#                break
#allsonglist=sorted(allsongpop.items(), key=lambda d: d[1])
# print allsonglist
# if allsonglist == {}:
#     print " "
# else:
#     print allsonglist[0:4]
sortednamelist=[]
name=raw_input()
namelist=trie.autocomplete(name)
for item in namelist:
    print allsongpop[item]
    sortednamelist.append(allsongpop[item])
sortednamelist=sorted(namelist.items(), key=lambda d: d[1])
print sortednamelist[0:4]
