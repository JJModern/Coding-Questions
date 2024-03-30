import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

# when string
f = [item.split() for item in f]


sys.setrecursionlimit(10**6)

from functools import lru_cache

@lru_cache
def rec():
    print("hi")

# C++ template
# g++ -std=c++17 hihi.cpp -o hihi
# ./acpcd
    
#include <iostream>
#include <vector>
#include <utility>
    
# int main() {
# }

#include <cctype>
    # std::isalpha()
    # isalpha()
    # toupper()
    # tolower()
    # isxdigit()
    # isupper()
    # isspace()
    # ispunct()
    # islower()
    # isdigit()
    # isblank()
    # isalpha()

#include <unordered_set>
    # std::unordered_set<int> myset;
