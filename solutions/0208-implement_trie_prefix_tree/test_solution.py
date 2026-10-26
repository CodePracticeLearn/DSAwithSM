from solution import Trie


def test_basic_operations():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.starts_with("app") == True
    trie.insert("app")
    assert trie.search("app") == True


def test_search_nonexistent():
    trie = Trie()
    trie.insert("hello")
    assert trie.search("hell") == False
    assert trie.search("helloo") == False
    assert trie.search("world") == False


def test_starts_with():
    trie = Trie()
    trie.insert("abc")
    assert trie.starts_with("a") == True
    assert trie.starts_with("ab") == True
    assert trie.starts_with("abc") == True
    assert trie.starts_with("abcd") == False
    assert trie.starts_with("b") == False


def test_empty_string():
    trie = Trie()
    trie.insert("")
    assert trie.search("") == True
    assert trie.starts_with("") == True


def test_multiple_words_shared_prefix():
    trie = Trie()
    trie.insert("car")
    trie.insert("card")
    trie.insert("care")
    trie.insert("careful")
    assert trie.search("car") == True
    assert trie.search("card") == True
    assert trie.search("care") == True
    assert trie.search("careful") == True
    assert trie.search("ca") == False
    assert trie.starts_with("car") == True
    assert trie.starts_with("care") == True
    assert trie.starts_with("caref") == True


def test_no_insertions():
    trie = Trie()
    assert trie.search("anything") == False
    assert trie.starts_with("a") == False
    assert trie.starts_with("") == True
