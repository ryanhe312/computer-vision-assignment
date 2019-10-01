import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
    
  N, D=X.shape
  D, C=W.shape

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores=X.dot(W)
  scores=(scores.T-np.amax(scores,axis=1)).T
  loss=-np.sum(scores[range(N),y])+np.sum(np.log(np.sum(np.exp(scores),axis=1)))
  loss/=N
  loss+=reg * np.sum(W*W)
    
  mask=np.zeros(scores.shape)
  mask[range(N),y]=-1
  mask+=(np.exp(scores).T/np.sum(np.exp(scores),axis=1)).T
  dW=(X.T).dot(mask)
  dW/=N
  dW+=reg * 2 * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  N, D=X.shape
  D, C=W.shape
    
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores=X.dot(W)
  scores=(scores.T-np.amax(scores,axis=1)).T
  loss=-np.sum(scores[range(N),y])+np.sum(np.log(np.sum(np.exp(scores),axis=1)))
  loss/=N
  loss+=reg * np.sum(W*W)
    
  mask=np.zeros(scores.shape)
  mask[range(N),y]=-1
  mask+=(np.exp(scores).T/np.sum(np.exp(scores),axis=1)).T
  dW=(X.T).dot(mask)
  dW/=N
  dW+=reg * 2 * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

