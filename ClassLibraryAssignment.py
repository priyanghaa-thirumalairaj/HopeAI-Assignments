class SubFieldsInAI:
    def subFields():
        listinput = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        for i in listinput:
            print(i)


class OddEven:
    def oddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")


class EligibilityForMarriage:
    @staticmethod
    def eligibleForMarriage(gender,age):
        if(gender == 'Male' and age >= 21):
            return True
        elif(gender == 'Female' and age >=18):
            return True
        else:
            return False
            
    @staticmethod        
    def eligible():
        gender = input("Enter your gender")
        age = int(input("Enter your age"))
        print("Your Gender:",gender)
        print("Your Age:",age)
        if(EligibilityForMarriage.eligibleForMarriage(gender,age)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
class FindPercent:
    @staticmethod
    def printSubjectMarks(subjectMarks):
        for index,subj in enumerate(subjectMarks,start=1):
            print(f"Subject{index}={subj}");
    @staticmethod
    def findTotalObtainedMarks(subjectMarks):
        total=0;
        for i in subjectMarks:
            total += i;
        return total;
    @staticmethod    
    def findTenthPercentage(total):      
        percen = (total/500)*100;
        return percen;
    @staticmethod    
    def percentage():
        subjectMarks =[];
        for i in range(0,5):
            sub = int(input("Enter the subject marks"));
            subjectMarks.append(sub);

        FindPercent.printSubjectMarks(subjectMarks);
        totalObtained=FindPercent.findTotalObtainedMarks(subjectMarks);
        print("Total=",totalObtained)
        print("Percentage=",FindPercent.findTenthPercentage(totalObtained))

class Triangle:
    @staticmethod
    def areaOfATriangle(base,height):
        return((base*height)/2)
    @staticmethod
    def perimeterOfATriangle(height1,height2,breadth):
        return(height1+height2+breadth)
    @staticmethod  
    def triangle():
        height=int(input("Enter the height of a triangle"))
        base=int(input("Enter the base of a triangle"))
        height1= int(input("Enter the height1 of a triangle"))
        height2= int(input("Enter the height2 of a triangle"))
        breadth= int(input("Enter the breadth of a triangle"))

        print("Height:",height)
        print("Breadth",base)
        print("Area Formula:(Height*Breadth)/2")
        print("Area of Triangle",Triangle.areaOfATriangle(base,height))
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth:",breadth)
        print("Perimeter Formula:Height1+Height2+Breadth")
        print("Perimeter of a triangle:",Triangle.perimeterOfATriangle(height1,height2,breadth))


        








            
        
   