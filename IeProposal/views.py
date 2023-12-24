from django.shortcuts import render

# Create your views here.
from IeProposal.proposal.proposalClass import *


def phone_post_proposal(request):
    content = ResetProposal(request,'phone_post_proposal')
    res = content.method_center()
    return res

def get_proposal(request):      #电脑端查看提案
    content = ResetProposal(request, 'get_proposal')
    res = content.method_center()
    return res
def proposal_options(request):
    content = ResetProposal(request,'proposal_options')
    res = content.method_center()
    return res

def get_confirm_proposal(request):
    content = ResetProposal(request, 'get_confirm_proposal')
    res = content.method_center()
    return res
def get_detailed_proposal(request):
    content = ResetProposal(request, 'get_detailed_proposal')
    res = content.method_center()
    return res
def download_file(request):
    content = ResetProposal(request, 'download_file')
    res = content.method_center()
    return res
def select_oa(request):
    content = ResetProposal(request, 'select_oa')
    res = content.method_center()
    return res
def down_proposal(request):
    content = ResetProposal(request, 'down_proposal')
    res = content.method_center()
    return res