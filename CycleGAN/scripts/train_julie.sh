python train.py --dataroot ./datasets/orangelip --name orange_transfer --model cycle_gan --niter 75 --niter_decay 25 --display_freq 20 --print_freq 50 --save_latest_freq 25 --save_epoch_freq 10 --transfer_net --transfer_name talebmu_cyclegan