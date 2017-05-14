PATH_TO_ATTRS = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Anno/list_attr_celeba.txt'
PATH_TO_IMGS = '/Users/govindadasu/Google Drive/SCHOOL-2016-2017/CS 231N - Convolutional Neural Netowrks/CelebA/Img/img_align_celeba/'

f = open(PATH_TO_ATTRS)

fm_w_lipstick = []
fm_wo_lipstick = []

for line in f:
	# print line
	line_attrs = line.split(' ')
	if len(line_attrs) > 20: 
		is_female = (line_attrs[20] == '-1')
		has_lipstick = (line_attrs[36] == '1')
		if is_female:
			print 'line_attrs[0]: ', line_attrs[0]
			print 'line_attrs[20]: ', line_attrs[20]
			if has_lipstick:
				fm_w_lipstick.append(line_attrs[0])
			else:
				fm_wo_lipstick.append(line_attrs[0])

print 'fm_w_lipstick: ', fm_w_lipstick
print 'fm_wo_lipstick: ', fm_wo_lipstick
