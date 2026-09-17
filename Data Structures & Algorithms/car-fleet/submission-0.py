class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        st = []
        cars = sorted(zip(position, speed))

        for pos, speed in cars:
            time = (target - pos) / speed

            while st and st[-1] <= time:
                st.pop()

            st.append(time)

        return len(st)
