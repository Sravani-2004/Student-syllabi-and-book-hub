#!/Python26/python
import re
import webbrowser
#import os 

    
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    
    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))
    
    # Checks that the required words are in the string
    for i in required_words:
      c=0
      for word in i:
        if word in user_message:
            c=1
            break
      if(c==0):
        has_required_words = False
        break
        
   
        
    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message,url=''):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello! How can I help you?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=[['how'],['you']])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('See you! Have a great day',['bye','goodbye'],single_response=True)
    response('Enter your semester number eg:sem 3',['year','sem','semester'],required_words=[['sem','semester'],['year']])
    response('sem1',['semester','sem','first','one','courses','list','subjects','1','sem1','1st'],required_words=[['courses','subjects'],['sem','semester','sem1','semester1'],['1','first','one','1st','sem1','semester1']])
    response('sem2',['semester','sem','second','two','courses','list','subjects','2','sem2','2nd'],required_words=[['courses','subjects'],['sem','semester','sem2','semester2'],['2','second','two','2nd','sem2','semester2']])
    response('sem3',['semester','3','third','3rd','courses','list','subjects','sem','three','sem3'],required_words=[['courses','subjects'],['3rd','3','sem3','three','semester3'],['semester','semester3','sem3','sem']])
    response('sem4',['semester','4','fourth','4th','courses','list','subjects','sem','four','sem4'],required_words=[['courses','subjects'],['4th','4','sem4','four','semester4'],['semester','semester4','sem4','sem']])
    response('sem5',['semester','sem','fifth','five','courses','list','subjects','5','sem5','5th'],required_words=[['courses','subjects'],['sem','semester','sem5','semester5'],['5','fifth','five','5st','sem5','semester5']])
    response('sem6',['semester','sem','sixth','six','courses','list','subjects','6','sem6','6th'],required_words=[['courses','subjects'],['sem','semester','sem2','semester2'],['6','sixth','six','6th','sem6','semester6']])
    response('sem7',['semester','7','seventh','7th','courses','list','subjects','sem','seven','sem7'],required_words=[['courses','subjects'],['7th','7','sem7','seven','semester3'],['semester','semester7','sem7','sem']])
    response('sem8',['semester','8','eighth','8th','courses','list','subjects','sem','eight','sem8'],required_words=[['courses','subjects'],['8th','8','sem8','eight','semester8'],['semester','semester8','sem8','sem']])
    response('lmath',['linear','algebra','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['linearalgebra','linear','mat211','la'],['mathematics','algebra','linearalgebra','mat211','maths','la']])    
    response('dmath',['discrete','mathematics','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['discretemathematics','discrete','mat141','dm'],['mathematics','maths','discretemathematics','mat141','dm']])  
    response('mmath',['multivariable','calculus','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['multi','multivariablecalculus','mat121','mvc'],['variable','mat121','multivariablecalculus','mvc'],['calculus','mat121','multivariablecalculus','mvc']])
    response('smath',['singlevariable','calculus','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['single','singlevariablecalculus','mat112','svc'],['variable','singlevariablecalculus','mat112','svc'],['calculus','mat112','singlevariablecalculus','svc']])
    response('difmath',['differentialequations','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['differentialequations','differential','mat131'],['differentialequations','equations','mat131']])
    response('pmath',['probabilityandstatisticsforengineers','probabilityandstatistics','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['probabilityandstatistics','probability','mat221'],['probabilityandstatistics','and','mat221'],['statistics','probabilityandstatistics','mat221']])
    response('eng',['communicativeenglish','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['communicative','communicativeenglish','egl101'],['communicativeenglish','english','egl101']])
    response('phy',['engineeringphysics','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['engineeringphysics','engineering','phy101','physics'],['physics','engineeringphysics','phy101']])
    response('che',['chemistryforegineers','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['chemistryforegineers','chemistry','che103'],['for','chemistryforegineers','chemistry','che103'],['chemistryforegineers','engineers','che103','chemistry']])
    response('psy',['psychology','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['psychology','hs'],['psychology','elective']])
    response('bio',['introductorybiology','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['introductorybiology','introductory','bio102'],['biology','introductorybiology','bio102']])
    response('evs',['environmentalscience','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['environmentalscience','environmental','env111'],['science','environmentalscience','env111']])
    response('cprog',['introductiontoprogrammingusingc','probabilityandstatistics','math','maths','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['introductiontiontoprogrammingusingc','c','cse105','cprogramming'],['introductiontoprogrammingusingc','cse105','programming']])
    response('iscp',['industrystandardcodingpractice','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['industrystandardcodingpractice','cse130','iscp']])
    response('ises',['industryspecificemployabilityskills','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['industryspecificemployabilityskills','ises','cse105']])
    response('oop',['objectorientedprogrammingwithc++','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['objectorientedprogrammingwithc++','oops','cse206','oop','c++'],['objectorientedprogrammingwithc++','cse206','programming','c++']])
    response('pyt',['handsonusingpython','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['hands','python','cse106l'],['on','cse106l','program','python'],['using','cse106l','python'],['python','cse106l','python']])
    response('daa',['designandanalysisofalgorithms','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['design','daa','cse201'],['and','cse201','daa'],['analysis','cse201','daa'],['of','cse201','daa'],['alogrithm','cse201','daa']])
    response('de',['digitalelectronics','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['digital','ece211','digitalelectronics'],['electronics','ece211','digitalelectronics']])
    response('be',['basicelectronics','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['basic','eng111','basicelectronics'],['electronics','eng111','basicelectronics']])
    response('ds',['datastructures','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['data','cse107','datastructures'],['structures','cse107','datastructures']])
    response('eco',['principlesofeconomics','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['principles','economics'],['and','economics','daa'],['analysis','economics','daa']])
    response('comp',['computerorganizationandarchitecture','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['computer','coa','cse204'],['organization','coa','cse204'],['and','cse204','coa'],['architecture','cse204','coa']])
    response('for',['formallanguagesandautomatatheory','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['formal','flat','cse203'],['automata','cse203','flat'],['and','cse203','flat'],['theroy','cse203','flat']])
    response('dms',['databasemanagementsystem','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['database','dms','cse304'],['management','cse304','dms'],['system','cse304','dms']])
    response('java',['javaprogramming','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['java','cse207'],['java','cse207','programming']])
    response('os',['operatingsystem','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['operating','cse301'],['system','cse301']])
    response('cn',['computernetworks','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['computer','cse303'],['networks','cse303']])
    response('cd',['compilerdesign','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['compiler','cse306'],['design','cse306']])
    response('se',['softwareengineering','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['software','cse305'],['engineering','cse305']])
    response('sy1',['syllabus','first','sem','semester','1st','sem1','1','one','portion'],required_words=[['1','first','one','1st','sem1','semester1'],['sem','semester','sem1','semester1'],['syllabus','portion']])
    response('sy2',['syllabus','second','sem','semester','2nd','sem2','2','two','portion'],required_words=[['2','second','two','2nd','sem2','semester2'],['sem','semester','sem2','semester2'],['syllabus','portion']])
    response('sy3',['syllabus','third','sem','semester','3rd','sem3','3','three','portion'],required_words=[['3','third','three','3rd','sem3','semester3'],['sem','semester','sem3','semester3'],['syllabus','portion']])
    response('sy4',['syllabus','fourth','sem','semester','4th','sem4','4','four','portion'],required_words=[['4','fourth','four','4th','sem4','semester4'],['sem','semester','sem4','semester4'],['syllabus','portion']])
    response('sy5',['syllabus','fifth','sem','semester','5th','sem5','5','five','portion'],required_words=[['5','fifth','five','5th','sem5','semester5'],['sem','semester','sem5','semester5'],['syllabus','portion']])                     
    response('sy6',['syllabus','sixth','sem','semester','6th','sem6','6','six','portion'],required_words=[['6','sixth','six','6th','sem6','semester6'],['sem','semester','sem6','semester6'],['syllabus','portion']])
    response('sy7',['syllabus','seventh','sem','semester','7th','sem7','7','seven','portion'],required_words=[['7','seventh','seven','7th','sem7','semester7'],['sem','semester','sem7','semester7'],['syllabus','portion']])
    response('sy8',['syllabus','eigth','sem','semester','8th','sem8','8','eight','portion'],required_words=[['8','eigth','eight','8th','sem8','semester8'],['sem','semester','sem8','semester8'],['syllabus','portion']])
    response('ises',['ises','industry','specific','employability','skills','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['ises','industry',],['specific','ises'],['employability','ises'],['skills','ises']])
    response('iscp',['iscp','industry','standard','coding','practice','text','book','books','textbook','textbooks','reference','references','referencebooks'],required_words=[['iscp','industry',],['standard','iscp'],['coding','iscp'],['practice','iscp']])
    response('help',['help'],single_response=True)
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #if(==0):
    #print(max(highest_prob_list.values()))

    if(max(highest_prob_list.values())==0):
        return "I'm sorry, I am unable to understand"
    #print('Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    else:
        return best_match
    
# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    if(len(response)==4 and response[0:3]=='sem'):
        x=response[3]
        
        url=str(r'course'+x+'.html')
        
        webbrowser.open(url)
    elif(response=='dmath'):
        url=str(r'course-3-m.html')
        webbrowser.open(url)
    elif(response=='oop'):
        url=str(r'course3-ios.html')
        webbrowser.open(url)
    elif(response=='daa'):
        url=str(r'course3-oppo.html')
        webbrowser.open(url)
    elif(response=='de'):
        url=str(r'course3-sraka.html')
        webbrowser.open(url)
    elif(response=='pyt'):
        url=str(r'course3_xyz.html')
        webbrowser.open(url)
    elif(response=='eco'):
        url=str(r'course3--wqq.html')
        webbrowser.open(url)
    elif(response=='mmath'):
        url=str(r'math.html')
        webbrowser.open(url)
    elif(response=='be'):
        url=str(r'be.html')
        webbrowser.open(url)
    elif(response=='ds'):
        url=str(r'ds.html')
        webbrowser.open(url)
    elif(response=='che'):
        url=str(r'che.html')
        webbrowser.open(url)
    elif(response=='evs'):
        url=str(r'evs.html')
        webbrowser.open(url)
    elif(response=='psy'):
        url=str(r'pyscho.html')
        webbrowser.open(url)
    elif(response=='eng'):
        url=str(r'english.html')
        webbrowser.open(url)
    elif(response=='smath'):
        url=str(r'abc.html')
        webbrowser.open(url)
    elif(response=='phy'):
        url=str(r'phy.html')
        webbrowser.open(url)
    elif(response=='bio'):
        url=str(r'bio.html')
        webbrowser.open(url)
    elif(response=='psy'):
        url=str(r'pyscho.html')
        webbrowser.open(url)
    elif(response=='pmath'):
        url=str(r'course4-a.html')
        webbrowser.open(url)
    elif(response=='difmath'):
        url=str(r'course4-b.html')
        webbrowser.open(url)
    elif(response=='comp'):
        url=str(r'course4-c.html')
        webbrowser.open(url)
    elif(response=='os'):
        url=str(r'course4-e.html')
        webbrowser.open(url)
    elif(response=='java'):
        url=str(r'course4-f.html')
        webbrowser.open(url)
    elif(response=='for'):
        url=str(r'course4-d.html')
        webbrowser.open(url)
    elif(response=='lmath'):
        url=str(r'linear algebra 22.html')
        webbrowser.open(url)
    elif(response=='cn'):
        url=str(r'comp_net.html')
        webbrowser.open(url)
    elif(response=='cd'):
        url=str(r'compiler_design.html')
        webbrowser.open(url)
    elif(response=='dms'):
        url=str(r'database_mang_sys.html')
        webbrowser.open(url)
    elif(response=='se'):
        url=str(r'software.html')
        webbrowser.open(url)
    elif(response=='ises'):
        url=str(r'course4-h.html')
        webbrowser.open(url)
    elif(response=='iscp'):
        url=str(r'course4-g.html')
        webbrowser.open(url)
    elif(response=='sy1'):
        url=str(r'https://drive.google.com/file/d/1SPxxblVDgnt0r8PZPn3iZu9rNc3bM9cm/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy2'):
        url=str(r'https://drive.google.com/file/d/1dmqNqxKP9bqKROPuBjBGBL5kpuAu0um9/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy3'):
        url=str(r'https://drive.google.com/file/d/1dq3TbbcgTWulAVZZkXTrzYYvOriyriua/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy4'):
        url=str(r'https://drive.google.com/file/d/1dsINvKf2uklhSWmVQphh1CgtnBPMxF5P/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy5'):
        url=str(r'https://drive.google.com/file/d/1dtSgmw2cmhlFVY6VNpbFuQ2FzDpUJNRK/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy6'):
        url=str(r'https://drive.google.com/file/d/1dtmNwzPHt4dUGHYBqmMHkl5eQElGxnqP/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy7'):
        url=str(r'https://drive.google.com/file/d/1dufTOiV9Nphnz1LSghclLIvWBQU1CkUd/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='sy8'):
        url=str(r'https://drive.google.com/file/d/1dufTOiV9Nphnz1LSghclLIvWBQU1CkUd/view?usp=sharing')
        webbrowser.open(url)
    elif(response=='ises'):
        webbrowser.open(r'course3-abc.html')
    elif(response=='iscp'):
        webbrowser.open(r'course3---bhk.html') 
    elif(response=='help'):
        print("To see the courses in any of the semesters:")
        print("Use keywords courses/subjects and sem / semester / sem1 / semester1 and 1 / first / one / 1st / sem1 / semester1 ")
        print("To see the syllabus of any semester:")
        print("Use keywords 3 / third / three / 3rd  and sem / semester / sem3 / semester3  and  syllabus / portion ")
        print("To open reference books :")
        print("Use keywords python / cse106l ")
    return response


# Testing the response system
print('Bot: Hi')
print('Bot: Enter "help" for guidelines:)')
while True:
    print('Bot: ' + get_response(input('You:')))
