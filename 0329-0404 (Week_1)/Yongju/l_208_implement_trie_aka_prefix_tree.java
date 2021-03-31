public class l_208_implement_trie_aka_prefix_tree {
  /**
   * Optimized solution
   *
   * key: Trie structure & its usage
   */
  class TrieNode {
      private final int R = 26;

      private TrieNode[] links;
      private boolean isEnd;

      public TrieNode() {
          links = new TrieNode[R];
      }

      public void put(char ch, TrieNode node) {
          links[ch - 'a'] = node;
      }

      public TrieNode get(char ch) {
          return links[ch - 'a'];
      }

      public boolean containsKey(char ch) {
          return links[ch - 'a'] != null;
      }

      public void setEnd() {
          isEnd = true;
      }

      public boolean isEnd() {
          return isEnd;
      }
  }

  class Trie {
      private TrieNode root;

      public Trie() {
          this.root = new TrieNode();
      }

      public void insert(String word) {
          TrieNode node = root;
          for (int i = 0; i < word.length(); ++i) {
              char curChar = word.charAt(i);
              if (!node.containsKey(curChar)) {
                  node.put(curChar, new TrieNode());
              }
              node = node.get(curChar);
          }
          node.setEnd();
      }

      public TrieNode searchPrefix(String word) {
          TrieNode node = root;
          for (int i = 0; i < word.length(); ++i) {
              char curChar = word.charAt(i);
              if (!root.containsKey(curChar)) {
                  return null;
              } else {
                  node = node.get(curChar);
              }
          }
          return node;
      }

      public boolean search(String word) {
          TrieNode node = searchPrefix(word);
          return node != null && node.isEnd();
      }

      public boolean startsWith(String prefix) {
          TrieNode node = searchPrefix(prefix);
          return node != null;
      }
  }
}
