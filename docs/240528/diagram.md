<div class="mermaid">
classDiagram
direction LR
    

    class Node {
        + key: int
        + value: Object
        - parent: Node
        - left: Node
        - right: Node
        + print_node()
    }

    class BST {
        + root: Node
        + search()
        + insert()
        + delete()
    }

    BST "1" o-- "*" Node
</div>  
