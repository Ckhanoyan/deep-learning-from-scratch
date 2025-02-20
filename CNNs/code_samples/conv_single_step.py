def conv_single_step(a_slice_prev, W, b):

    s = a_slice_prev * W
    Z = np.sum(s)
    Z = Z + float(b)

    return Z
