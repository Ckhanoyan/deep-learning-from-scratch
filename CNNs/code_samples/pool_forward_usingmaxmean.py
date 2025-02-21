def pool_forward(A_prev, hparameters, mode = "max"):
   
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    f = hparameters["f"]
    stride = hparameters["stride"]
    
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    n_C = n_C_prev
    
    A = np.zeros((m, n_H, n_W, n_C))              
    
    for i in range(m):
        for h in range(n_H):
            vert_start = h * stride
            vert_end = vert_start + f
            
            for w in range(n_W):
                horiz_start = w * stride
                horiz_end = horiz_end + f
                
                for c in range(n_C):
                    a_prev_slice = a_prev[vert_start:vert_end, horiz_start:horiz_end, :]
                    
                    if mode == "max":
                        A[i, h, w, c] = np.max(a_prev_slice)
                    elif mode == "average":
                        A[i, h, w, c] = np.mean(a_prev_slice)
                
    cache = (A_prev, hparameters)
    
    return A, cache
