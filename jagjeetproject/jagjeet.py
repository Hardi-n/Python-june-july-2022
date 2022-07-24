line1 = FigureCanvasTkAgg(fig1, root)
line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
age = data['Age']
dev_salaries = data['All_Devs']
python_salaries = data['Python']
js_salaries = data['JavaScript']

root= tk.Tk()
fig1, (ax1)= plt.subplots(nrows=1, ncols=1, sharey = True)

line1 = FigureCanvasTkAgg(fig1, root)
line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.plot(age, dev_salaries, label = 'All Devs', linestyle='--', color='red')
root.mainloop()