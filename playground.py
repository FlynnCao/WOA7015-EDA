# if is 1 or 5, use 120 freq_lo_resp = 0.5 freq_hi_resp = 5 # 5 time_ecg = np.arange(x_ecg.shape[0])dt_ecg1000 time_resp = np.arange(x_resp.shape[0])*dt_resp plt.figure(figsize=(16,5)) plt.scatter(time_ecg, x_ecg, color = 'hotpink',s=2)
freq_lo_ecg = 20
freq_hi_ecg = 125
plt.scatter(time_resp, x_resp, color='#88c999')
x_ecg_filter = bp_filter(x_ecg, fs_ecg, freq_lo_ecg, freq_hi_ecg)
plt.xlabel("TIME STAMP")
plt.ylabel("Signal")
plt.scatter(time_ecg, x_ecg_filter, color='green', s=2)
plt.title("Fliter function")
plt.show()
