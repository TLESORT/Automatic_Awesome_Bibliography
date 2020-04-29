## Outline 
- [Rehearsal](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Rehearsal)
- [Generative-Replay](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Generative-Replay)
- [Dynamic-Architecture](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Dynamic-Architecture)
- [Regularization](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Regularization)
- [Meta-Learning](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Meta-Learning)
- [Replay](https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Classification_Bibliography.md#Replay)

## Rehearsal
- **Efficient Lifelong Learning with A-GEM**, (2019) [[paper]](https://arxiv.org/abs/1812.00420)  [[bib]](../bibtex.bib#L25-L32)  by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed*
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Orthogonal Gradient Descent for Continual Learning**, (2019) [[paper]](https://arxiv.org/abs/1910.07104)  [[bib]](../bibtex.bib#L373-L382)  by *Mehrdad Farajtabar, Navid Azizan, Alex Mott and Ang Li*
``` 
projecting the gradients from new tasks onto a subspace in which the neural network output on previous task does not change and the projected gradient is still in a useful direction for learning the new task
``` 
- **Gradient based sample selection for online continual learning**, (2019) [[paper]](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf)  [[bib]](../bibtex.bib#L386-L396)  by *Aljundi, Rahaf, Lin, Min, Goujaud, Baptiste and Bengio, Yoshua*
``` 
sample selection as a constraint reduction problem based on the constrained optimization view of continual learning
``` 
- **Online Continual Learning with Maximal Interfered Retrieval**, (2019) [[paper]](http://papers.nips.cc/paper/9357-online-continual-learning-with-maximal-interfered-retrieval.pdf)  [[bib]](../bibtex.bib#L400-L410)  by *Aljundi, Rahaf, Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo, Lin, Min, Charlin, Laurent and Tuytelaars, Tinne*
``` 
Controlled sampling of memories for replay to automatically rehearse on tasks currently undergoing the most forgetting
``` 
- **Online Learned Continual Compression with Adaptative Quantization Module**, (2019) [[paper]](https://arxiv.org/abs/1911.08019)  [[bib]](../bibtex.bib#L414-L421)  by *Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo and Pineau, Joelle*
``` 
Uses stacks of VQ-VAE modules to progressively compress the data stream, enabling better rehearsal
``` 
- **Experience replay for continual learning**, (2019) [[paper]](https://arxiv.org/abs/1811.11682)  [[bib]](../bibtex.bib#L1022-L1030)  by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory*
- **Gradient Episodic Memory for Continual Learning**, (2017) [[paper]](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf)  [[bib]](../bibtex.bib#L47-L57)  by *Lopez-Paz, David and Ranzato, Marc-Aurelio*
``` 
A model that alliviates CF via constrained optimization
``` 
- **icarl: Incremental classifier and representation learning**, (2017) [[paper]](https://arxiv.org/abs/1611.07725)  [[bib]](../bibtex.bib#L663-L671)  by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H*
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Generative Replay
- **Generative Models from the perspective of Continual Learning**, (2019) [[paper]](https://hal.archives-ouvertes.fr/hal-01951954)  [[bib]](../bibtex.bib#L527-L539)  by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David*
``` 
Extensive evaluation of CL methods for generative modeling
``` 
- **Marginal replay vs conditional replay for continual learning**, (2019) [[paper]](https://arxiv.org/abs/1810.12069)  [[bib]](../bibtex.bib#L967-L976)  by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David*
``` 
Extensive evaluation of generative replay methods
``` 
- **Generative replay with feedback connections as a general strategy for continual learning**, (2018) [[paper]](https://arxiv.org/abs/1809.10635)  [[bib]](../bibtex.bib#L425-L433)  by *Michiel van der Ven and Andreas S. Tolias*
``` 
smarter Generative Replay
``` 
- **Continual learning with deep generative replay**, (2017) [[paper]](https://arxiv.org/abs/1705.08690)  [[bib]](../bibtex.bib#L61-L69)  by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon*
``` 
Introduces generative replay
``` 

## Dynamic Architecture
- **ORACLE: Order Robust Adaptive Continual Learning**, (2019) [[paper]](http://arxiv.org/abs/1902.09432)  [[bib]](../bibtex.bib#L171-L187)  by *Jaehong Yoon and
Saehoon Kim and
Eunho Yang and
Sung Ju Hwang*
- **Random Path Selection for Incremental Learning**, (2019) [[paper]](http://arxiv.org/abs/1906.01120)  [[bib]](../bibtex.bib#L192-L209)  by *Jathushan Rajasegaran and
Munawar Hayat and
Salman H. Khan and
Fahad Shahbaz Khan and
Ling Shao*
``` 
Proposes a random path selection algorithm, called RPSnet, that progressively chooses optimal paths for the new tasks while encouraging parameter sharing and reuse
``` 
- **Incremental Learning through Deep Adaptation**, (2018) [[paper]](https://openreview.net/forum?id=ryj0790hb)  [[bib]](../bibtex.bib#L347-L353)  by *Amir Rosenfeld and John K. Tsotsos*
- **Progressive Neural Networks**, (2016) [[paper]](https://arxiv.org/abs/1606.04671)  [[bib]](../bibtex.bib#L355-L370)  by *{Rusu}, A.~A., {Rabinowitz}, N.~C., {Desjardins}, G., 
{Soyer}, H., {Kirkpatrick}, J., {Kavukcuoglu}, K., 
{Pascanu}, R. and {Hadsell}, R.*
``` 
Each task have a specific model connected to the previous ones
``` 

## Regularization
- **Continual Learning with Bayesian Neural Networks for Non-Stationary Data**, (2020) [[paper]](https://openreview.net/forum?id=SJlsFpVtDB)  [[bib]](../bibtex.bib#L461-L468)  by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann*
``` 
continual learning for non-stationary data using Bayesian neural networks and memory-based online variational Bayes
``` 
- **Improving and Understanding Variational Continual Learning**, (2019) [[paper]](https://arxiv.org/abs/1905.02099)  [[bib]](../bibtex.bib#L125-L133)  by *Siddharth Swaroop, Cuong V. Nguyen, Thang D. Bui and Richard E. Turner*
``` 
Improved results and interpretation of VCL.
``` 
- **Uncertainty-based Continual Learning with Adaptive Regularization**, (2019) [[paper]](http://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf)  [[bib]](../bibtex.bib#L146-L156)  by *Ahn, Hongjoon, Cha, Sungmin, Lee, Donggyu and Moon, Taesup*
``` 
Introduces VCL with uncertainty measured for neurons instead of weights.
``` 
- **Functional Regularisation for Continual Learning with Gaussian Processes**, (2019) [[paper]](https://arxiv.org/abs/1901.11356)  [[bib]](../bibtex.bib#L917-L924)  by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye*
``` 
functional regularisation for Continual Learning: avoids forgetting a previous task by constructing and memorising an approximate posterior belief over the underlying task-specific function
``` 
- **Task Agnostic Continual Learning Using Online Variational Bayes**, (2018) [[paper]](https://arxiv.org/pdf/1803.10123.pdf)  [[bib]](../bibtex.bib#L159-L168)  by *Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry*
``` 
Introduces an optimizer for CL that relies on closed form updates of mu and sigma of BNN; introduce label trick for class learning (single-head)
``` 
- **Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation**, (2018) [[paper]](https://openreview.net/forum?id=B1al7jg0b)  [[bib]](../bibtex.bib#L215-L222)  by *Xu He and Herbert Jaeger*
``` 
Conceptor-Aided Backprop (CAB): gradients are shielded by conceptors against degradation of previously learned tasks
``` 
- **Overcoming Catastrophic Forgetting with Hard Attention to the Task**, (2018) [[paper]](http://proceedings.mlr.press/v80/serra18a.html)  [[bib]](../bibtex.bib#L235-L251)  by *Serra, Joan, Suris, Didac, Miron, Marius and Karatzoglou, Alexandros*
``` 
Introducing a hard attention idea with binary masks
``` 
- **Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence**, (2018) [[paper]](https://arxiv.org/abs/1801.10112)  [[bib]](../bibtex.bib#L254-L261)  by *Chaudhry, Arslan, Dokania, Puneet K, Ajanthan, Thalaiyasingam and Torr, Philip HS*
``` 
Formalizes the shortcomings of multi-head evaluation, as well as the importance of replay in single-head setup. Presenting an improved version of EWC.
``` 
- **Variational Continual Learning**, (2018) [[paper]](https://arxiv.org/abs/1710.10628)  [[bib]](../bibtex.bib#L285-L292)  by *Cuong V. Nguyen, Yingzhen Li, Thang D. Bui and Richard E. Turner*
``` 
Introduces the idea of using previous task's posterior as the new task's prior in a BNN.
``` 
- **Progress \& compress: A scalable framework for continual learning**, (2018) [[paper]](https://arxiv.org/abs/1805.06370)  [[bib]](../bibtex.bib#L296-L303)  by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia*
``` 
A new P\&C architecture; online EWC for keeping the knowledge about the previous task, knowledge for keeping the knowledge about the current task (Multi-head setting, RL)
``` 
- **Overcoming catastrophic forgetting in neural networks**, (2017) [[paper]](https://www.pnas.org/content/pnas/114/13/3521.full.pdf)  [[bib]](../bibtex.bib#L35-L43)  by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others*
``` 
Introduces prior-focused methods (Elastic Weight Consolidation)
``` 
- **Memory Aware Synapses: Learning what (not) to forget**, (2017) [[paper]](http://arxiv.org/abs/1711.09601)  [[bib]](../bibtex.bib#L267-L280)  by *Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars*
``` 
Importance of parameter measured based on their contribution to change in the learned prediction function
``` 
- **Continual Learning Through Synaptic Intelligence**, (2017) [[paper]](http://proceedings.mlr.press/v70/zenke17a.html)  [[bib]](../bibtex.bib#L306-L321)  by *Zenke, Friedeman, Poole, Ben and Ganguli, Surya *
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 

## Meta-Learning
- **Learning to Continually Learn**, (2020) [[paper]](https://arxiv.org/abs/2002.09571)  [[bib]](../bibtex.bib#L992-L999)  by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick*
``` 
Follow-up of OML. Meta-learns an activation-gating function instead.
``` 
- **Online Fast Adaptation and Knowledge Accumulation: a New Approach to Continual Learning**, (2020) [[paper]](https://arxiv.org/abs/2003.05856)  [[bib]](../bibtex.bib#L1034-L1041)  by *Caccia, Massimo, Rodriguez, Pau, Ostapenko, Oleksiy, Normandin, Fabrice, Lin, Min, Caccia, Lucas, Laradji, Issam, Rish, Irina, Lacoste, Alexandre, Vazquez, David and others*
``` 
Proposes a new approach to CL evaluation more aligned with real-life applications, bringing CL closer to Online Learning and Open-World learning
``` 
- **Meta-Learning Representations for Continual Learning**, (2019) [[paper]](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning.pdf)  [[bib]](../bibtex.bib#L436-L446)  by *Javed, Khurram and White, Martha*
``` 
Introduces Learns how to continually learn (OML) i.e. learns how to do online updates without forgetting.
``` 
- **Learning from the Past: Continual Meta-Learning via Bayesian Graph Modeling**, (2019) [[paper]](https://arxiv.org/abs/1911.04695)  [[bib]](../bibtex.bib#L449-L458)  by *Yadan Luo, Zi Huang, Zheng Zhang, Ziwei Wang, Mahsa Baktashmotlagh and Yang Yang*
- **Online Meta-Learning**, (2019) [[paper]](http://proceedings.mlr.press/v97/finn19a.html)  [[bib]](../bibtex.bib#L471-L486)  by *Finn, Chelsea, Rajeswaran, Aravind, Kakade, Sham and Levine, Sergey*
``` 
defines Online Meta-learning; propsoses Follow the Meta Leader (FTML) (~ Online MAML)
``` 
- **Reconciling meta-learning and continual learning with online mixtures of tasks**, (2019) [[paper]](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks.pdf)  [[bib]](../bibtex.bib#L490-L500)  by *Jerfel, Ghassen, Grant, Erin, Griffiths, Tom and Heller, Katherine A*
``` 
Meta-learns a tasks structure; continual adaptation via non-parametric prior
``` 
- **Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based RL**, (2019) [[paper]](https://openreview.net/forum?id=HyxAfnA5tm)  [[bib]](../bibtex.bib#L505-L512)  by *Anusha Nagabandi, Chelsea Finn and Sergey Levine*
``` 
Formulates an online learning procedure that uses SGD to update model parameters, and an EM with a Chinese restaurant process prior to develop and maintain a mixture of models to handle non-stationary task distribution
``` 
- **Meta-learnt priors slow down catastrophic forgetting in neural networks**, (2019) [[paper]](https://arxiv.org/pdf/1909.04170.pdf)  [[bib]](../bibtex.bib#L1002-L1009)  by *Spigler, Giacomo*
``` 
Learning MAML in a Meta continual learning way slows down forgetting
``` 
- **Learning to learn without forgetting by maximizing transfer and minimizing interference**, (2018) [[paper]](https://arxiv.org/abs/1810.11910)  [[bib]](../bibtex.bib#L1013-L1020)  by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald*

## Replay
- **Generative Models from the perspective of Continual Learning**, (2019) [[paper]](https://hal.archives-ouvertes.fr/hal-01951954)  [[bib]](../bibtex.bib#L527-L539)  by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David*
``` 
Extensive evaluation of CL methods for generative modeling
``` 
- **Marginal replay vs conditional replay for continual learning**, (2019) [[paper]](https://arxiv.org/abs/1810.12069)  [[bib]](../bibtex.bib#L967-L976)  by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David*
``` 
Extensive evaluation of generative replay methods
``` 
- **Generative replay with feedback connections as a general strategy for continual learning**, (2018) [[paper]](https://arxiv.org/abs/1809.10635)  [[bib]](../bibtex.bib#L425-L433)  by *Michiel van der Ven and Andreas S. Tolias*
``` 
smarter Generative Replay
``` 
- **Continual learning with deep generative replay**, (2017) [[paper]](https://arxiv.org/abs/1705.08690)  [[bib]](../bibtex.bib#L61-L69)  by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon*
``` 
Introduces generative replay
``` 
