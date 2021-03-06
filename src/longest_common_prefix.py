# coding: utf-8
#                                                    ##       ##
#                                                  #####   #  ####
#                                               ######### ## #######
#                                              ###  ############ ##
#                               ####          #     ####### #########
#  ###########               #########       #      ###########  ##
# #############             ###    ####        ##  #### ########                                     ##
# ##   ##    ##            ##        ###     #########  #########        ###         ##       #     ###      ##      #
#      ##   ##                    ## ###    ########   ##########       #### ##     ###     ####   ###    #####    ####
#     ## ####                     ##  ##   #########   ##########      ########    #####   ####    ####   #####   #####
#    ######          ####        ##   ##  ### ## ###  ############    ## ### ##   ## ##   ###      ###    #####  ### ##
#    ####           #####        ##  ###  ###  ###### ############       ##  ##  #####    ### ##  ###     ###    #####
#   ## ##         ### ###       ###  ###   ######### ##############     ### ##   ####     ## ###  #####  ####    ####
#   ## ###        ##  ##        ##  ###     #####    ##############    #######    #####   #####   #####  ###     ######
#  ##   ###  ##  #######        ######              ###############    ####         ##     ##       #              ###
#  ##   ######   #######       #####               #################   ###
# ##      ###     ##  ##       ###                  #################  ##
# ##                           ##                 ###################  ##
# ##                          ###                  ######################
#                             ##                    #               ## #
#                             ##
# author: RaPoSpectre
# time: 2016-11-09

# 动态规划, 复杂度 O(n2), 状态是: n 个字符串 n < len(strs) 的最长公共前缀, 转移方程: D(n) = min{D(n-1), L(j)}, 0 <= j <= min{D(n-1), len(str(n))} (大概是这样)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max = -1
        last = 0
        if not len(strs):
            return ''
        for i, itm in enumerate(strs):
            if max == -1:
                max = len(itm)
            else:
                cl = min(max, len(itm))
                tmp = 0
                for j in xrange(1, cl + 1):
                    if itm[:j] == strs[last][:j]:
                        tmp = j
                    else:
                        break
                if tmp < max:
                    max = tmp
                last = i
        return strs[0][:max]

# print Solution().longestCommonPrefix(['a','b','c'])
