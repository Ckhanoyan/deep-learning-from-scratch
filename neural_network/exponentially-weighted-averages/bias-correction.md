# Why Bias Correction is Needed

Bias correction is important when you are working with EWAs in machine learning because sometimes at the beginning of the process, the average may be biaseds towards zero. Because there has not been enough data yet to stabilize the moving average. This can lead to a misleading estimate. As a result, we need to adjust the early values by correcting this bias, making them more accurate as we accumulate more data. The bias corrected version of the EWAs is below: 

<img width="400" alt="{740E165F-F182-45A6-86AB-56242FEBAE7C}" src="https://github.com/user-attachments/assets/7e9fe38a-c044-435d-b308-516a747bb40a" />

Where: 
* vt is the EWA at time step t
* beta is the smoothing factor
* t is the time step or iteration number
* 1 - beta t is the bias correction term

### How do we use this formula and incorporate into the existing example code? 

<img width="800" alt="{28E76B1E-552B-4186-BBBA-D25C0B70ABD2}" src="https://github.com/user-attachments/assets/3ed7cc82-4bf2-4ddc-9943-2a9a05b85407" />

Ah ha! Do you notice something from this outcome? This bias correction fixed the initial underestimation that occurs when the moving average is first computed (look at the EMA.py and EWA-bias-correction.py and compare the first steps from each other). This ensures the average becomes more accurate over time, particularly when you are early in the sequence. 

Isn't it great?
