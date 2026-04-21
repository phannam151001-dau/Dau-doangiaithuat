class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(heights, names))
        people.sort(reverse=True)
        return [name for _, name in people]