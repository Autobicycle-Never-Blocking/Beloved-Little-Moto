# # def get_skill(df):
#
#
#
# position_names = n_lagou['positionName'].tolist()
# skill_lables = n_lagou['skillLables'].tolist()
#
# from collections import defaultdict
# skill_position_graph = defaultdict(list)
# for p, s in zip(position_names, skill_lables):
#     skill_position_graph[p] += eval(s)
#
# import networkx as nx
#
# G = nx.Graph(skill_position_graph)
#
# pr = nx.pagerank(G, alpha=0.9)
# ranked_position_and_ability = sorted([(name, value) for name, value in pr.items()],
#                                      key=lambda x: x[1],
#                                     reverse=True)