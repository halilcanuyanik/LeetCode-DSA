/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

let carry = 0;

var addTwoNumbers = function(l1, l2) {
    if (!l1 && !l2 && carry === 0) {
        return null;
    }
    const val1 = l1 ? l1.val : 0;
    const val2 = l2 ? l2.val : 0;

    let sum = val1 + val2 + carry;
    carry = sum >= 10 ? 1 : 0;
    sum = sum % 10;

    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;

    const nextNode = addTwoNumbers(l1, l2);
    return new ListNode(sum, nextNode);
};