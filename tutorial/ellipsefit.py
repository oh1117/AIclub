
# mask: a 2D binary mask
plt.imshow(mask,cmap='gray')

# fit an ellipse to mask
ellipse=get_ellipse(mask)
(c,r),(b,a),alfa=ellipse # (c,r) center coordinate, (b,a) major and minor radius, alfa: rotation angle

## create a binary mask from the fitted ellipse
elipse_mask=np.zeros_like(mask)
cv2.ellipse(elipse_mask, ellipse, (255,0, 0), -1) # elipse mask 



## split ellipse into two circles or ellipses
# centers of two circles/ellipses
c1=(c-a/4*np.sin(alfa))
r1=(r+b/4*np.cos(alfa))
c2=(c+a/4*np.sin(alfa))
r2=(r-b/4*np.cos(alfa))

# coodiates of ellipses
ellipse1=((c1,r1),(b/2,a/2),alfa)
ellipse2=((c2,r2),(b/2,a/2),alfa)

# coordinates of circles
radius=int(a/4)
c1=int(c1)
c2=int(c2)
r1=int(r1)
r2=int(r2)

## split to two circles
two_circle_mask=np.zeros_like(mask)
cv2.circle(two_circle_mask,(c1,r1), radius, (255,0,255), -1)
cv2.circle(two_circle_mask,(c2,r2), radius, (255,0,255), -1)

## split to two ellipses
two_ellipse_mask=np.zeros_like(mask)
cv2.ellipse(two_ellipse_mask, ellipse1, (255,0, 0), -1)
v2.ellipse(two_ellipse_mask, ellipse2, (255,0, 255), -1)

# plots
plt.subplot(132)
plt.imshow(two_circle_mask)

plt.subplot(133)
plt.imshow(two_ellipse_mask)


## Passing functions with multiple return values as arguments in Python

# function definition
def func1(x1,y1):
  #your code
  return r1,t1

# function definition
def func2(x2,y2):
  #your code
  return r2,rt

# main code
func2(*func1(x1,y1))

