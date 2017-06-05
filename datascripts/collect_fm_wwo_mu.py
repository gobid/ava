from subprocess import call

PATH_TO_ATTRS = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Anno/list_attr_celeba.txt'
PATH_TO_IMGS = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/img_align_celeba/'
DEST_FOR_FMWLP = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/fm_w_lipstick/'
DEST_FOR_FMWOLP = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/fm_wo_lipstick/'

DEST_FOR_FMWBH = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/fm_w_blondh/'
DEST_FOR_FMWOBH = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/fm_wo_blondh/'

f = open(PATH_TO_ATTRS)

fm_w_lipstick = []
fm_wo_lipstick = []

fm_w_blondh = []
fm_wo_blondh = []

for line in f:
	# print line
	line_attrs = line.split()
	#print 'line_attrs len: ', len(line_attrs)
	if len(line_attrs) > 36 and line_attrs[0] == '5_o_Clock_Shadow': 
		print 'line_attrs[20]: ', line_attrs[20]
		print 'line_attrs[-4]: ', line_attrs[-4]
	elif len(line_attrs) > 37: 
		#print 'line_attrs: ', line_attrs
		#print 'line_attrs[0]: ', line_attrs[0]
		#print 'line_attrs[21]: ', line_attrs[21]
		#print 'line_attrs[-4]: ', line_attrs[-4]
		is_female = (line_attrs[21] == '-1')
		has_lipstick = (line_attrs[37] == '1')
		is_blond = (line_attrs[10] == '1')
		if is_female:
			if has_lipstick:
				fm_w_lipstick.append(line_attrs[0])
			else:
				fm_wo_lipstick.append(line_attrs[0])
			if is_blond:
				fm_w_blondh.append(line_attrs[0])
			else:
				fm_wo_blondh.append(line_attrs[0])
	else:
		print '1sts line ... '

#print 'fm_w_lipstick: ', fm_w_lipstick
#print 'fm_wo_lipstick: ', fm_wo_lipstick

print 'fm_w_blondh: ', fm_w_blondh
print 'fm_wo_blondh: ', fm_wo_blondh

#for p in fm_w_lipstick: 
#	call(['sudo', 'cp', PATH_TO_IMGS + '/' + p, DEST_FOR_FMWLP])

#for p in fm_wo_lipstick: 
#	call(['sudo', 'cp', PATH_TO_IMGS + '/' + p, DEST_FOR_FMWOLP])

# for p in fm_w_blondh: 
#	call(['sudo', 'cp', PATH_TO_IMGS + '/' + p, DEST_FOR_FMWBH])

for p in fm_wo_blondh: 
	call(['sudo', 'cp', PATH_TO_IMGS + '/' + p, DEST_FOR_FMWOBH])
