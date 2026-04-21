class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        max_alt = 0
        for g in gain:
            altitude += g
            max_alt = max(max_alt, altitude)
        return max_alt
        