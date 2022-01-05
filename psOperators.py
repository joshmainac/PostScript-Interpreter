from psItems import Value, ArrayValue, FunctionValue
#Joshua Long
class Operators:
    def __init__(self,scoperule):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        self.scope = scoperule
        #The builtin operators supported by our interpreter
        self.builtin_operators = {
            "stack":self.stack,
            "cleanTop":self.cleanTop,
            "opPop":self.opPop,
            "opPush":self.opPush,

            "mydict":self.mydict,
            "lookup":self.lookup,
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "mod":self.mod,
            "eq":self.eq,
            "lt":self.lt,
            "gt":self.gt,
            "length":self.length,
            "getinterval":self.getinterval,
            "putinterval":self.putinterval,
            "aload":self.aload,
            "astore":self.astore,
            "pop":self.pop,
            "dup":self.dup,
            "copy":self.copy,
            "count":self.count,
            "clear":self.clear,
            "exch":self.exch,
            "roll":self.roll,
            
            "psDict":self.psDict,

            "define":self.psDef,
            "def":self.psDef,
            "psIf":self.psIf,
            "psIfelse":self.psIfelse,
            "repeat":self.repeat,
            "forall":self.forall,
            "clearBoth":self.clearBoth,
            "if":self.psIf,
            "psIf":self.psIf,
            "ifelse":self.psIfelse,
            "psIfelse":self.psIfelse,
            "myscope":self.myscope





            
             # TO-DO in part1
             # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator. 
             # Make sure **not to call the functions** 
             #watch video 47:12, make function list
             #erased dict begin end
             # "dictPop":self.dictPop,
             # "dictPush":self.dictPush,
             # "begin":self.begin,
             # "end":self.end,
             # "dict":self.psDict,
        }
    #-------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()

    #my additional custom function
    def myscope(self):
        print(self.scope)


    ##My comment
    def opPop(self):
        if len(self.opstack) > 0:
            x = self.opstack[len(self.opstack) - 1]
            self.opstack.pop(len(self.opstack) - 1)
            return x
        else:
            return {}#not sure about this,doing this for test_dict

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)
        
    #------- Dict Stack Operators --------------
    
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """   
    #HW5 change it
    def dictPop(self):
        #not sure
        return self.dictstack.pop(-1)

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    #HW5 change it (self,index,d),package index and d as a tuple then push it
    # def dictPush(self,d):
    #     self.dictstack.append(d)

    def dictPush(self,index,d):
        myvalue= (index,d)
        self.dictstack.append(myvalue)        

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """  
    #HW5 change it (seld,index,name, value)??make it work for tuple,maybe not change argumentss
    # def define(self,name, value):
    #     self.dictstack[-1][name]=value

    def define(self,name, value):
        self.dictstack[-1][1][name]=value        

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    ##Mycomment
    ##use get() to look it for
    #HW5 change it do name evaluate first
    #make 2 lookup or add an argument
    #if static jump around using index
    # def lookup(self,name):
    #     for d in reversed(self.dictstack):
    #         if d.get('/' + name, None) != None:
    #             return d.get('/' + name, None)
    #     return None

    def lookup(self,name):
        if self.scope == "static":    
            def staticLink(self,myfunc):

                #check top node if function exist if not follow the link
                #psstacks.dictstack[-1][1] will return the top dict
                #mod it
                def staticLink(self,myfunc,index):
                    mylist = self.dictstack
                    index = mylist.index(mylist[index])#so it deals with negative num
                    if '/'+myfunc in mylist[index][1]:
                        #print("found it at index:",index)////list(mylist[index][1].keys())[0]//if mylist[index][1] ==myfunc:
                        return index
                    else:
                        if index == mylist[index][0]:
                            #print("not found")
                            return 0
                        else: 
                            #print(mylist[index][0]) 
                            return staticLink(self,myfunc,mylist[index][0])  
                ans = staticLink(self,myfunc,-1) 
                return ans
            myindex = staticLink(self,name)  
            mytuple = self.dictstack[myindex][1].get('/' + name, None)
            if mytuple ==None:
                print("Error 201  ",end="")
                print("finding: ", name)
                print(self.dictstack[myindex])

                return None
            else:
                return mytuple              
          
            # #print("Look up static link")#mod it #not sure about the below if
            # if self.dictstack[-1][1].get('/' + name, None) !=None:
            #     return self.dictstack[-1][1].get('/' + name, None)

            # myindex = self.dictstack[-1][0]
            # mytuple = self.dictstack[myindex][1].get('/' + name, None)
            # if mytuple ==None:
            #     print("Error 201  ",end="")
            #     print("finding: ", name)
            #     print(self.dictstack[myindex])

            #     return None
            # else:
            #     return mytuple
        else:
            for i,j in reversed(self.dictstack):
                 if j.get('/' + name, None) != None:
                      return j.get('/' + name, None)
            return None  
        
           
               
              
    
    #------- Arithmetic Operators --------------
    
    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """  
    ##Mycomment 
    def add(self):
        op2 = self.opPop()
        op1 = self.opPop()
        self.opPush(op1 + op2)

 
    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """   
    def sub(self):
        op2 = self.opPop()
        op1 = self.opPop()
        self.opPush(op1 - op2)



    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """    
    def mul(self):
        op2 = self.opPop()
        op1 = self.opPop()
        self.opPush(op1 * op2)

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """ 
    def mod(self):
        op2 = self.opPop()
        op1 = self.opPop()
        self.opPush(op1 % op2)       
    #---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """ 
    def eq(self):
        op2 = self.opPop()
        op1 = self.opPop()
        if(op2 == op1):
            self.opPush(True) 
        else:
            self.opPush(False)    

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """ 
    def lt(self):
        op2 = self.opPop()
        op1 = self.opPop()
        if(op1<op2):
            self.opPush(True) 
        else:
            self.opPush(False)

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """ 
    def gt(self):
        op2 = self.opPop()
        op1 = self.opPop()
        if(op1>op2):
            self.opPush(True) 
        else:
            self.opPush(False)

    # ------- Array Operators --------------
    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """
    def length(self):
        mylist = self.opPop()
        self.opPush(len(mylist.value))

 

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """
    ##mycomment
    ##pop 3 variables,then re create the list and push it
    def getinterval(self):
        count = self.opPop()
        index = self.opPop()
        mylist = self.opPop()
        newlist = mylist.value[index:(index+count)]
        newlist2 = ArrayValue(newlist)
        self.opPush(newlist2)

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """
    ##mycomment
    ##pop the 3 values and rewrite will arr1
    def putinterval(self):
        mylist2 = self.opPop()
        index = self.opPop()
        arr1 = self.opPop()
        arr1.value[index:index+len(mylist2.value)]=mylist2.value
        #self.opPush(arr1)




            

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """
    ##mycomments
    ##pop the list and push all the value
    ##
    def aload(self):
        op = self.opPop()
        for i in op.value:
            self.opPush(i)
        self.opPush(op)    
        
    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """

    def astore(self):
        op = self.opPop()
        mylen= len(op.value)
        while(len(self.opstack) >= mylen):
            i =0
            d = []
            while (i<mylen):
                d.append(self.opPop())
                i = i+1
            d.reverse()    
            self.opPush(ArrayValue(d))  
            if len(self.opstack) == mylen:
                break
            



                

    #------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        self.opPop()

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    # def stack(self):
    #     for i in reversed(self.opstack):
    #         print(i)

    def stack(self):
        print("===**opstack**===")
        for i in reversed(self.opstack):
            print(i) 
        print("===**dictstack**===") 
        mylen = len(self.dictstack)
        for i in reversed(self.dictstack):
            mylen = mylen -1
            print("----%d----%d----"%(mylen,i[0]))
            #print the dict content
            if(i[1]=={}):
                pass

            else:
                mydict = i[1]
                for i in mydict:
                    print(i,end="")
                    print("  ",end="")
                    print(mydict[i])


            
                      

    def mydict(self):
        if len(self.dictstack)>0:
            head = self.dictstack[-1]
            print(head)
        else:
            print("Empty")    

        


    """
       Copies the top element in opstack.
    """
    def dup(self):
        op1 = self.opPop()
        self.opPush(op1)
        self.opPush(op1)


    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        count = self.opPop()
        mylist = self.opstack[-count:]
        for ii in mylist:
            self.opPush(ii)


    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    ##mycomment
    def count(self):
        mynum = len(self.opstack)
        self.opPush(mynum)

    """
       Clears the opstack.
    """
    def clear(self):
        self.opstack.clear()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        op2 = self.opPop()
        op1 = self.opPop()
        self.opPush(op2)
        self.opPush(op1)

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    def roll(self):
        count = self.opPop()
        index = self.opPop()
        givenlist = self.opstack
        templist2 = givenlist[-index:]
        templist1 = givenlist[:-index]
        if count > 0:
            appendlist2 = templist2[-count:]
            appendlist1 = templist2[:-count]
            newlist= templist1+ appendlist2+appendlist1  
            self.opstack= newlist[:]
        else:
            appendlist1 = templist2[:-count]
            appendlist2 = templist2[-count:]
            newlist= templist1+ appendlist2+appendlist1  
            self.opstack= newlist[:]


             


    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """
    #change for HW5
    # def psDict(self):
    #     myint = self.opPop()
    #     mydict = {}
    #     self.opPush(mydict)

    def psDict(self):
        myint = self.opPop()
        mydict = {}
        self.opPush(mydict)        

    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """
    #change for HW5
    # def begin(self):
    #     dic = self.opPop()
    #     self.dictPush(dic)

    def begin(self):
         dic = self.opPop()
         self.dictPush(0,dic)    
        

    """
       Removes the top dictionary from dictstack.
    """
    def end(self):
        self.dictstack.pop(-1)
        
    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """
    #change for HW5
    # def psDef(self):
    #     if len(self.dictstack) ==0:
    #         self.dictstack.append({})
    #     value = self.opPop()
    #     name = self.opPop()
    #     self.dictstack[-1][name]=value

    def psDef(self):
        if len(self.dictstack) ==0:
            self.dictPush(0,{})
        value = self.opPop()
        name = self.opPop()
        #self.dictstack[-1][name]=value  
        self.define(name,value)  
        


    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
       
    """
    #HW5 change it mod apply method
    def psIf(self):
        #
        if len(self.opstack) > 1:
            cond_statement = self.opPop()
            bool_op = self.opPop()
            if(bool_op == True):
                myindex = len(self.dictstack)-1
                cond_statement.apply_function(self,myindex)#apply(self, psstacks)
                #cond_statement.apply(self)

        else:
            print("Not enough operands on the stack")


    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """
    #HW5 change it mod apply method
    def psIfelse(self):
            if len(self.opstack) > 1:
                #
                cond_False = self.opPop()
                cond_True = self.opPop()
                bool_op = self.opPop()
                if(bool_op == True):
                    myindex = len(self.dictstack)-1
                    cond_True.apply_function(self,myindex)#apply(self, psstacks)
                    #cond_True.apply(self)
                elif(bool_op == False):
                    myindex = len(self.dictstack)-1
                    cond_False.apply_function(self,myindex)#apply(self, psstacks)
                    #cond_False.apply(self)
            else:
                print("Not enough operands on the stack")




    #------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """  
    #HW5 change it mod apply method
    def repeat(self):
        if len(self.opstack) > 1:
            cond_statement = self.opPop()
            #bool_op = self.opPop()
            count = self.opPop()
            for i in range(0,count):
                myindex = len(self.dictstack)-1
                cond_statement.apply_function(self,myindex)#apply(self, psstacks)
                #cond_statement.apply(self)
        else:
            print("Not enough operands on the stack")
        
    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """ 
    #HW5 change it mod apply method
    #apply(self,len(self.dictstack)-1) which is the index of the top tuple
    def forall(self):
        if len(self.opstack) > 1:
            myfunc = self.opPop()
            #bool_op = self.opPop()
            myarray = self.opPop()
            for i in myarray.apply_list(self):
                self.opPush(i)
                myindex = len(self.dictstack)-1
                myfunc.apply_function(self,myindex)
                #myfunc.apply(self)
        else:
            print("Not enough operands on the stack")        

    #--- used in the setup of unittests 
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []
