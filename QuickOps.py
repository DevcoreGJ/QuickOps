class ListOperator:
    def __init__(self, lst):
        self.lst = lst

    def sumvar(self, target):
        indices = []
        for i, val in enumerate(self.lst):
            if target - val in self.lst[:i] + self.lst[i+1:]:
                indices.append(i)
        return indices

class StringOperator:
    def __init__(self, s):
        self.s = s

    def noRepCharSub(self):
        substr = ""
        max_substr = ""
        for char in self.s:
            if char not in substr:
                substr += char
            else:
                substr = substr[substr.index(char)+1:] + char
            if len(substr) > len(max_substr):
                max_substr = substr
        return max_substr

class ListStringOperator:
    def __init__(self, lst_or_str):
        if isinstance(lst_or_str, list):
            self.operator = ListOperator(lst_or_str)
        elif isinstance(lst_or_str, str):
            self.operator = StringOperator(lst_or_str)
        else:
            raise TypeError("Input must be a list or a string.")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListMerge:
    def MergeHeads(self, head1: ListNode, head2: ListNode) -> ListNode:
        # Initialize the new linked list
        merged_list = ListNode(None)
        current_node = merged_list

        # Merge the two linked lists
        while head1 and head2:
            if head1.val <= head2.val:
                current_node.next = head1
                head1 = head1.next
            else:
                current_node.next = head2
                head2 = head2.next
            current_node = current_node.next

        # Append the remaining nodes of the longer list
        if head1:
            current_node.next = head1
        else:
            current_node.next = head2

        return merged_list.next

