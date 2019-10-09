This code is based on the paper: A Nonenegative Matrix Factorization Approach for Multiple Local Community Detection published in the ASONAM conference in 2018.


To run  the code with the sample Amazon network:
(1) with cmd go to the code folder
(2) pip install -r requirements.txt
(3) go to MLC folder
(4)python MLC.py
(5) go to MLC-code folder, you will find the conductance results in the Cond folder and the F1 results in the F1 folder.

NOTE: 

(a) graphA is Amazon while graphD is DBLP.

(b) To run this code on a different graph, change the following variables:
	graphFiles=['graphA.txt'] 	#Amazon
	communityFile='newComA.txt' 	#cleaned ground-truth communities with duplicates removed
        seedsFiles=['seedsA3.txt'] 	#seeds that belong to three communities
        delimiter = "\t" 		#delimiter of the graph's edge list. For some graphs, it is just blank space " "

The data folder contains other sample graphs and seeds, and their ground-truth communities. 
Karate club is not included in the graphs folder as it can be generated using: G = nx.karate_club_graph()



Citation (BibTex format):

@article{Kamuhanda2018ANM,
  title={A Nonnegative Matrix Factorization Approach for Multiple Local Community Detection},
  author={Dany Kamuhanda and Kun He},
  journal={2018 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM)},
  year={2018},
  pages={642-649}
}