/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy;  // Previous distinct node

        while (head) {
            // Check if current node has duplicates
            if (head->next && head->val == head->next->val) {
                // Skip all nodes with the same value
                while (head->next && head->val == head->next->val) {
                    head = head->next;
                }
                // Link previous node to the next distinct node
                prev->next = head->next;
            } else {
                // Move previous node pointer if there were no duplicates
                prev = prev->next;
            }
            // Move head to the next node
            head = head->next;
        }

        // Return the new head, which is dummy->next
        return dummy->next;
    }
};