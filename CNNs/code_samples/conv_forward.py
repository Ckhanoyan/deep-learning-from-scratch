
def conv_forward(A_prev, W, b, hparameters):

    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    (f, f, n_C_prev, n_C) = W.shape
    
    stride = hparameters["stride"]
    pad = hparameters["pad"]
    
    n_H = int((n_H_prev - f + 2 * pad) // stride + 1)
    n_W = int((n_W_prev - f + 2 * pad) // stride + 1)
    
    Z = np.zeros((m, n_H, n_W, n_C))
    
    a_prev_pad = np.pad(A_prev, ((0,), (pad, ), (pad, ), (0,)), mode = 'constant', constant_values = 0)
    
    for i in range(m):
        a_prev_example = a_prev_pad[i]
        
        for h in range(n_H):
            vert_start = h * stride
            vert_end = vert_start + f
            
            for w in range(n_W):
                horiz_start = w * stride 
                horiz_end = horiz_start + f
                
                for c in range(n_C): 
                    a_slice_prev = a_prev_example[vert_start:vert_end, horiz_start:horiz_end, :]
                    weights = W[:, :, :, c]
                    biases = b[:, :, :, c]
                    Z[i, h, w, c] = np.sum(a_slice_prev * weights) + float(biases)
    
    cache = (A_prev, W, b, hparameters)
    
    return Z, cache
