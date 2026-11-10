import base64,json,os
s=open('src-index.html').read()
d={f[:-4]:base64.b64encode(open('sounds/'+f,'rb').read()).decode() for f in sorted(os.listdir('sounds')) if f.endswith('.mp3')}
bg=base64.b64encode(open('art/start-background.jpg','rb').read()).decode() if os.path.exists('art/start-background.jpg') else ''
open('index.html','w').write(s.replace('{/*__SND__*/}',json.dumps(d)).replace('/*__BG__*/',bg));print(len(d),'sounds',os.path.getsize('index.html'))
