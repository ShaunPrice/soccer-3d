import base64,json,os
s=open('src-index.html').read()
d={f[:-4]:base64.b64encode(open('sounds/'+f,'rb').read()).decode() for f in sorted(os.listdir('sounds')) if f.endswith('.mp3')}
open('index.html','w').write(s.replace('{/*__SND__*/}',json.dumps(d)));print(len(d),'sounds',os.path.getsize('index.html'))
