class Solution:
    def f(self, spell, potions, success):
        i, j = 0, len(potions)
        while i < j:
            mid = (i + j) // 2
            if potions[mid] * spell >= success:
                j = mid
            else:
                i = mid + 1
        return len(potions) - i

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [self.f(spell, potions, success) for spell in spells]
