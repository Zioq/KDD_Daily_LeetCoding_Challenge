public class l_211_design_add_and_search_words_data_structure {
  class WordDictionary {

      private TrieNode root;

      /** Initialize your data structure here. */
      public WordDictionary() {
          root = new TrieNode();
      }

      public void addWord(String word) {
          TrieNode node = root;
          for (int i = 0; i < word.length(); ++i) {
              char curChar = word.charAt(i);
              if (!node.containsKey(curChar)) {
                  node.add(curChar, new TrieNode());
              }
              node = node.get(curChar);
          }
          /**
           * To filter substrings
           */
          node.word = word;
      }

      public boolean search(String word) {
          return searchHelper(word.toCharArray(), root, 0);
      }

      /**
       * Recursive solution
       */
      public boolean searchHelper(char[] chars, TrieNode root, int index) {
          TrieNode node = root;
          /**
           * if we return true instead of checking word, it can't filter substrings
           */
          if (chars.length == index) return node.word != null;

          char curChar = chars[index];
          if (curChar != '.') {
              return root.get(curChar) != null && searchHelper(chars, root.get(curChar), index + 1);
          } else {
              for (TrieNode trieNode : node.getChildren()) {
                  if (trieNode != null)
                      if (searchHelper(chars, trieNode, index + 1)) return true;
              }
          }
          return false;
      }

      class TrieNode {

          private final int R = 26;
          private TrieNode[] links;
          /**
           * word: need to keep this variable to check if it is the end of word
           *      -> can be replace with a boolean value
           */
          public String word;

          public TrieNode() {
              links = new TrieNode[R];
          }

          public void add(char c, TrieNode node) {
              links[c - 'a'] = node;
          }

          public boolean containsKey(char c) {
              return links[c - 'a'] != null;
          }

          public TrieNode get(char c) {
              return links[c - 'a'];
          }

          public TrieNode[] getChildren() {
              return links;
          }
      }
  }
}
