import re
text='sreeramBALAmuruGAN'
m=re.search('BALA(.+?)GAN',text)
if m:
     found=m.group(1)
     print found
