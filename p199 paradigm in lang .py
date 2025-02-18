procedural = ["C", "Fortran", "Pascal", "Ada", "BASIC", "Algol", "COBOL", "Rust"]
object_oriented = ["Java", "C++", "Python", "Ruby", "C#", "Swift", "Objective-C", "Dart"]
functional = ["Haskell", "Scala", "Lisp", "Erlang", "F#", "OCaml", "Elixir", "Racket"]

lang=input("Enter language =>").capitalize()

if lang in procedural:
    print("It is procedural langauge")
elif lang in object_oriented:
    print("It is  object_oriented")
elif lang in functional:
    print("It is  functional")
else:
    print("None of above")