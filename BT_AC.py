import new_arc as arc
import numpy as np
import time as t
import copy

def check_mult(N,V,maxv,space):
	if(space<1):
		return False
	# print("N {} ,V {} ,maxv {} ,space {}".format(N,V,maxv,space))
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	# print(vals)
	# print("space is",space)
	NV=V;
	if(V%N==0):
		NV=V/N
	# print("NV is {}".format(NV))
		if(space==1):
			if NV in vals:
				return True
			else:
				return False
		else:
			for v in vals:
				if(NV%v==0):
					# print("NV {}, v {}".format(NV,v))
					if (check_mult(v,NV,maxv,space-1)):
						return True

	return False

# def check_mult_rep(space,N,V):
# 	if(space==2):
# 		if(V/N==N):
# 			return False
# 		else:
# 			return True

# 	else:
# 		return check_mult_rep(space-1,N,V/N)




def mult_vals(maxv,space,V):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	p_vals=[]
	p=[]
	space=space-1
	for N in vals:
		if(check_mult(N,V,maxv,space)):
			p_vals.append(N)





	return p_vals


def check_add(N,V,maxv,space):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	# print(vals)
	# print("space is",space)
	# NV=V;
	# if(V%N==0):
	NV=V-N
	# print("NV is {}".format(NV))
	if(space==1):
		if NV in vals:
			return True
		else:
			return False
	else:
		for v in vals:
			if(NV>v):
				# print("NV {}, v {}".format(NV,v))
				if (check_add(v,NV,maxv,space-1)):
					return True

	return False


def add_vals(maxv,space,V):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	p_vals=[]
	space=space-1
	for N in vals:
		if(check_add(N,V,maxv,space)):
			p_vals.append(N)

	return p_vals





def check_sub(N,V,maxv):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)

	if (N-V) in vals:
		return True
	elif (N+V) in vals:
		return True
	else:
		return False


def sub_vals(maxv,V):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	p_vals=[]
	# space=space-1
	for N in vals:
		if(check_sub(N,V,maxv)):
			p_vals.append(N)

	return p_vals


def check_div(N,V,maxv):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)

	if (N/V) in vals:
		return True
	elif (N*V) in vals:
		return True
	else:
		return False


def div_vals(maxv,space,V):
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	p_vals=[]
	space=space-1
	for N in vals:
		if(check_div(N,V,maxv)):
			p_vals.append(N)

	return p_vals







def cage_valid(N,cage,maxv):
	values=cage[0]
	avl=len(values)-np.count_nonzero(values)

	if((cage[2]=='+')|(cage[2]=='*')):
		if(N>cage[1]):	
			return False

	if(cage[2]=='+'):
		if(N==cage[1]):
			if(len(cage[0])==1):
				return True
			if(len(cage[0])>1):
				return False

		if(N<cage[1]):
			if(avl==1):
				if(N==(cage[1]-np.sum(values))):
					return True
				else:
					return False
			else:
				return check_add(N,cage[1]-np.sum(values),maxv,avl-1)
		else:
			return False


	if(cage[2]=='-'):
		if(avl==1):
				if(N>max(values)):
					if(N==(cage[1]+np.sum(values))):
						return True
					else:
						return False
				else:
					if(max(values)==(np.sum(values)-max(values)+N+cage[1])):
						return True
					else:
						return False

		else:
			return check_sub(N,cage[1],maxv)






		

	if(cage[2]=='*'):
		nz_values=[i for i in values if i!=0]
		# #print("non zero",np.prod(nz_values))
		if(avl==1):
			if(N>cage[1]):
				return False
			elif(N==cage[1]):
				if(max(values)==1):
					return True
				else:
					return False
			else:
				if(cage[1]==(N*np.prod(nz_values))):
					return True
				else:
					return False
		else:
			return(check_mult(N,int(cage[1]/np.prod(nz_values)),maxv,avl-1))
			


	if(cage[2]=='/'):
		if(avl==1):
			if((N/max(values)==cage[1])|(max(values)/N==cage[1])):
				return True
			else:
				return False

		else:
			return check_div(N,cage[1],maxv)



def check_equal_list(ls1,ls2):
	if(len(ls1)==len(ls2)):
		if(len(list(set(ls1)-set(ls2)))==0&len(list(set(ls2)-set(ls1)))==0):
			return True

	return False


def i2it(i,j,max):
	return (i*max)+j


def it2i(it,max):
	return(int(it/max),int(it%max))

def twin(proboard):
	# print("twin\n")
	table=[]
	done=[[],[]]
	for i in range(len(proboard)):
		for j in range(len(proboard)):
			it=(i*len(proboard))+j
			tt=()
			points=[it]
			values=[]
			if it not in done[0]:
				done[0].append(it)
				if type(proboard[i][j]) is list:
					for x in range(len(proboard)-1-j):
						if type(proboard[i][j+1+x]) is list:
							# print("equal probs",i,j)

							if(check_equal_list(proboard[i][j],proboard[i][j+1+x])):

								values=proboard[i][j]
								points.append(i2it(i,j+x+1,len(proboard)))
								done[0].append(i2it(i,j+x+1,len(proboard)))
								# print(i,j+1+x)
								# print("values points hor",values,points)
			# print(done,i,j)

			if(len(values)==len(points)):
				tt=(values,0,points)
				table.append(tt)
			values=[]
			points=[it]

			if it not in done[1]:
				done[1].append(it)
				if type(proboard[i][j]) is list:
					for x in range(len(proboard)-1-i):
						if type(proboard[i+1+x][j]) is list:
							if(check_equal_list(proboard[i][j],proboard[i+1+x][j])):
								values=proboard[i][j]
								done[1].append(i2it(i+1+x,j,len(proboard)))
								points.append(i2it(i+1+x,j,len(proboard)))
								# print ("equals",i,i+1+x,j)
								# print("values points vir",values,points)

				if(len(values)==len(points)):
					tt=(values,1,points)
					table.append(tt)
			values=[]
			points=[]


	return table



def update_twin(board,proboard,table,cages,cells):
	# print("update\n")
	itrs=list(range(len(board)))
	vals=list(np.asarray(itrs)+1)
	for tt in table:
		# print("tt ", tt)

		points=[[],[]]
		for it in tt[2]:
			(i,j)=it2i(it,len(board))
			points[0].append(i)
			points[1].append(j)
		# print("points ",points)

		if(tt[1]==0):
			i=points[0][0]
			upvals=tt[0]
			its=list(set(itrs)-set(points[1]))
			for j in its:
				if type(proboard[i][j]) is not list:
					continue
				#print("i ",i,"j ",j)
				fvals=list(set(proboard[i][j])-set(upvals))
				# print("fvals ",fvals)
				if(len(fvals)==1):
					board[i][j]=fvals[0]
					proboard[i][j]=fvals[0]
					try:
						cages[cells[i][j]][0].remove(0)
						cages[cells[i][j]][0].append(fvals[0])
					except:
						1

				else:
					if type(proboard[i][j]) is list:
						proboard[i][j]=list(set(fvals).intersection(proboard[i][j]))


		if(tt[1]==1):
			j=points[1][0]
			upvals=tt[0]
			
			its=list(set(itrs)-set(points[0]))
			# print("to be updated",its,"\n")
			for i in its:
				if type(proboard[i][j]) is not list:
					continue
				#print("i ",i,"j ",j)
				fvals=list(set(proboard[i][j])-set(upvals))
				#print("fvals ",fvals)
				if(len(fvals)==1):
					board[i][j]=fvals[0]
					proboard[i][j]=fvals[0]
					try:
						cages[cells[i][j]][0].remove(0)
						cages[cells[i][j]][0].append(fvals[0])
					except:
						1

				else:
					if type(proboard[i][j]) is list:
						proboard[i][j]=list(set(fvals).intersection(proboard[i][j]))
			

def cage_values(cage,proboard):
	if 0 in cage[0]:
		probs=[]
		for it in cage[3]:
			(i,j)=it2i(it,len(proboard))
			if type(proboard[i][j]) is list:
				probs=list(set(probs+proboard[i][j]))

		updated_probs=[]

		for N in probs:
			if(cage_valid(N,cage,len(proboard))):
				updated_probs.append(N)

		for it in cage[3]:
			(i,j)=it2i(it,len(proboard))
			if type(proboard[i][j]) is list:
				proboard[i][j]=list(set(updated_probs).intersection(proboard[i][j]))


def update_cages(cages,proboard):
	for cage in cages:
		cage_values(cage,proboard)

def update_board(proboard,board):
	for i in range(len(board)):
		for j in range(len(board)):
			if type(proboard[i][j]) is list:
				if (len(proboard[i][j])==1):
					board[i][j]=proboard[i][j][0]
					proboard[i][j]=proboard[i][j][0]

def q_valid(board,r,c):
	maxv=len(board)
	vals=list(range(maxv))
	vals=list(np.asarray(vals)+1)
	row=[]
	col=[]
	zero=[0]
	for i in range(len(board)):
		row.append(board[r][i])
		col.append(board[i][c])

	rvals=list(set(vals)-set(row))
	final_vals=list(set(rvals)-set(col))
	# #print("qVals are",final_vals)
	return final_vals



def probs(board,cages,cells):
	# print("probability\n",board)
	proboard=copy.deepcopy(board)
	num_zero=len(board)**2-np.count_nonzero(board)
	old_num_zero=0
	iterations=0
	# while(num_zero>0):
		# old_num_zero=num_zero
	for i in range(len(board)):
		for j in range(len(board)):
			# print(i,j)
			if(board[i][j]==0):
				# print("({},{})".format(i,j))
				p_vals=[]
				cage=cages[cells[i][j]]
				#print(cage)
				vals=q_valid(board,i,j)
				# print("qvals\n",vals)
				# if(len(vals)==1):
				# 	print("final value")
				# 	board[i][j]=vals[0]
				# 	proboard[i][j]=vals[0]
				# 	num_zero-=1
				# 	try:
				# 		cage[0].remove(0)
				# 		cage[0].append(vals[0])
				# 	except:
				# 		# print("no zero")
				# 		1

				# 	continue


				for N in vals:
					# print("cage ",cage)
					if(cage_valid(N,cage,len(board))):
						p_vals.append(N)
				

				# if type(p_vals) is int:

				# print("pvals {} , cage {}".format(p_vals,cage))

				if(len(p_vals)==1):
					board[i][j]=p_vals[0]
					proboard[i][j]=p_vals[0]
					num_zero-=1
					try:
						cage[0].remove(0)
						cage[0].append(p_vals[0])
					except:
						# print("no zero")
						1
				else:
					proboard[i][j]=p_vals
					# print(p_vals)
			else:
				if(board[i][j]!=0):
					temp=board[i][j]
					# print(" only one possibility",temp)
					proboard[i][j]=temp


					#print(board)
			#print(proboard)

	# while(num_zero>0):



	return proboard


def rep_update(board,proboard,cages,cells):
	old_num_zero=0
	iterations=0
	num_zero=len(board)**2-np.count_nonzero(board)
	while(num_zero>0):
		if(iterations>5):
			break
		num_zero=len(board)**2-np.count_nonzero(board)
		if(num_zero==old_num_zero):
			iterations+=1

		else:
			old_num_zero=num_zero
		proboard=probs(board,cages,cells)
		table=twin(proboard)
		# print("table",table)
		update_twin(board,proboard,table,cages,cells)
		# print("proboard after twin ",proboard)
		update_cages(cages,proboard)
		# print("proboard after cage ",proboard)
		update_board(proboard,board)
		# print("board",board)
		# print("proboard",proboard)
		# print("row,col",row,col,type(proboard[row][col]))


def check_empty(proboard):
	# print("empty")
	for i in range(len(proboard)):
		for j in range(len(proboard)):
			if type(proboard[i][j]) is list:
				if(len(proboard[i][j])==0):
					return True

	
	return False


def solve(board,proboard,it,cages,cells):
	#print("into function",it)
	#print("board",board)
	

	# //system("cls");
	# //printSudoku9x9(arr);
	row=int(it/len(board))
	col=int(it%len(board))
	
	if(check_empty(proboard)):
		return (False,None)

	if (row > len(board)-1):
		#print("done")
		return (True,board);

	# print("board",board)
	if (board[row][col] > 0):
		(b,OB)=solve(board,proboard,it+1,cages,cells)
		if(b):
			# board=copy.deepcopy(boardcopy
			# proboard=copy.deepcopy(probcopy)
			# cages=copy.deepcopy(cagescopy)
			#print("r",it,True)
			#print("board",OB)
			return (True,OB)


	if (check_empty(proboard)):
		return (False,None)
	#print("it2222",it,type(proboard[row][col]),"\n\n\n\n\n\n")
	if (check_empty(proboard)):
		return (False,None)

	#print("proboard ",proboard)
	
	status = (False,None)
	probcopy= copy.deepcopy(proboard)
	boardcopy=copy.deepcopy(board)
	cagescopy=copy.deepcopy(cages)
	rep_update(board,proboard,cages,cells)
	
	if type(proboard[row][col]) is list:
		#print("list")
		if (len(proboard[row][col]) == 0):
			return (False,None)
		status = (False,None)
		#print("board",board)
		if(len(board)**2-np.count_nonzero(board)==0):
				#print("no zeros",it)
				status= True
				OB=board
				#print("board",OB)
				return (True,OB)
		for i in proboard[row][col]:

			# print("it",it,"N",i)
			# if(it==3&i==5):
			#print("\n\n\n\n\n\n\n\n\n\n\n\n")
			# print("board",board)
			# print("probabili/ties",proboard)
			#print(cages)
			n = i
			# probcopy= copy.deepcopy(proboard)
			boardcopy=copy.deepcopy(board)
			cagescopy=copy.deepcopy(cages)
			boardcopy[row][col] = n
			try:
				cagescopy[cells[row][col]][0].remove(0)
				cagescopy[cells[row][col]][0].append(n)
			except:
				return (False,None)
			#print("copy",boardcopy)
			#print("cages",cages)
			probcopy=probs(boardcopy,cagescopy,cells)
			#print("before check",probcopy)
			if( probcopy[row][col]==0 | probcopy[row][col]==[]):
				return (False,None)
			# print("probs copy",probcopy)
			(b,OB)=solve(boardcopy,probcopy,it+1,cagescopy,cells)
			if (b):
				#print(" it {} ,True\n\n\n\n\n\n\n\n".format(it))
				board=copy.copy(boardcopy)
				proboard=copy.copy(probcopy)
				# OB=boardcopy
				
				return (True,OB)
				break
		#print("break")
	if type(proboard[row][col]) is not list:
		#print("int")
		if(proboard[row][col]>0):
			probcopy= copy.deepcopy(proboard)
			boardcopy=copy.deepcopy(board)
			cagescopy=copy.deepcopy(cages)
			# //cout << "(" << row << "," << col << ") =>" << n << endl;
			# boardcopy[row][col] = n;
			(b,OB)=solve(boardcopy,probcopy,it+1,cagescopy,cells)
			if (b):
				status = (True,OB)
		else:
			status=(False,None)
	if(len(board)**2-np.count_nonzero(board)>0):
		status= (False,None)
	if(len(board)**2-np.count_nonzero(board)==0):
		#print("no zeros\n\n\n\n\n\n\n\n\n\n\n\n",it)
		status= True

	
	#print("it,status",it,status)
	#print("board",board)
	return status;


def solve_kenken(size,cages):
	board=[[0]*size]*size
	l_cages=[]
	cells=[[0]*size]*size
	for cage in cages:
		its=[]
		vals=[]
		op=cage[1]
		V=cage[2]
		for p in cage[0]:
			it=i2it(p[0],p[1],size)
			its.append(it)
			vals.append(0)
			cells[p[0]][p[1]]=len(l_cages)
		l_cage=(vals,int(cage[2]),cage[1],its)
		l_cages.append(l_cage)

	proboard=probs(board,l_cages,cells)

	(b,OB)=arc.solve(board,proboard,0,l_cages,cells)
	if(b):
		return OB
	else:
		return None






