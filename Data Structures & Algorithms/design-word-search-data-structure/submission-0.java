public class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for(char c : word.toCharArray()){
            int idx = c - 'a';
            if(node.children[idx]==null){
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root,0,word);
    }

    public boolean dfs(TrieNode root, int j, String word){
        TrieNode node = root;
        for(int i=j;i<word.length();i++){
            if(word.charAt(i)=='.'){
                for(TrieNode child : node.children){
                    if(child != null && dfs(child,i+1,word)){
                        return true;
                    }
                }
                return false;
            }
            else{
                int idx = word.charAt(i) - 'a';
                if(node.children[idx]==null){
                    return false;
                }
                node = node.children[idx];
            }
        }
        return node.isEnd;
    }
}
