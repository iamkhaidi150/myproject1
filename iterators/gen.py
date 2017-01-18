#!/usr/bin/env python
import psutil,random,time
names=['john','corey','adam','steve','rick','thomas']
majors=['math','engineering','compsci','arts','business']
print 'Memory (Before):{} bytes and in % is {}%'.format(psutil.virtual_memory()[1],psutil.virtual_memory()[2])
def people_list(num_people):
    result=[]
    for i in xrange(num_people):
        person = {
                'id':i,
                'name':random.choice(names),
                'major':random.choice(majors)
            }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                'id': i,
                'name': random.choice(names),
                'major':random.choice(majors)
            }
        yield person
#t1=time.clock()
#people=people_list(1000000)
#t2=time.clock()

t1=time.clock()
people=people_generator(1000000)
print people
print type(people)
print next(people)
print next(people)
t2=time.clock()

print 'Memory (After): {} bytes and in  % is {}%'.format(psutil.virtual_memory()[1],psutil.virtual_memory()[2])
print 'Took {} Seconds'.format(t2-t1)
