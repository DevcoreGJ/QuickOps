from QuickOps import ListOperator, StringOperator, ListStringOperator, ListNode, ListMerge

# return the indices that add up to a target variable or dictionary list entry. 
my_list = [1, 3, 4, 2, 6, 7, 5]
lst_op = ListOperator(my_list)
indices = lst_op.sumvar(10)
print(indices)  # Output: [1, 4]

# Find longest non repeating substring in string
my_string = "abcabcbb"
str_op = StringOperator(my_string)
longest_sub = str_op.noRepCharSub()
print(longest_sub)  # Output: "abc"

# Create two sorted linked lists
head1 = ListNode(1, ListNode(3, ListNode(5)))
head2 = ListNode(2, ListNode(4, ListNode(6)))

# Merge the two linked lists
list_merge = ListMerge()
merged_head = list_merge.MergeHeads(head1, head2)

# Print the new linked list
current_node = merged_head
while current_node:
    print(current_node.val)
    current_node = current_node.next
