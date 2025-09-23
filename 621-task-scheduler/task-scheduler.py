class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        d= Counter(tasks)
        fmax = max(d.values())
        k = sum(1 for i in d.values() if i==fmax)
        frame_based_time = (fmax - 1) * (n + 1) + k
        return max(len(tasks),frame_based_time)