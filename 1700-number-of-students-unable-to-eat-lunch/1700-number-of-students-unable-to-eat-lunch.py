class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_count = Counter(students)
        san_count = Counter(sandwiches)
        
        students = deque(students)
        sandwiches = sandwiches[::-1]
        
        while True:
            while sandwiches and students and students[0] == sandwiches[-1]:
                stu_count[students.popleft()]-=1
                san_count[sandwiches.pop()]-=1
            
            if not students or not sandwiches:
                return len(students)
            
            if stu_count[sandwiches[-1]]<=0:
                return len(students)
            
            students.append(students.popleft())
        return len(student)