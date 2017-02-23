import random
import os
import numpy as np
import math


videos = []
requests = []
endpoints = []
cache_servers = []

def process_file(input_file):
    global videos
    global requests
    global endpoints
    global cache_servers

    with open(input_file, 'r') as f:
        # TODO Implement.


class CacheServer(object):

    def __init__(self, identifier, max_capacity):
        self.max_capacity = max_capacity
        self.identifier = identifier
        self.current_capacity = 0
        self.videos = {}
        self.num_videos = 0

    def get_identifier(self):
        return self.identifier

    def max_capacity(self):
        return self.max_capacity

    def current_capacity(self):
        return self.current_capacity

    def get_videos(self):
        return self.videos

    def num_videos(self):
        return self.num_videos

    def add_video(self, video):
        self.videos[video.get_identifier()] = video
        self.current_capacity += video.get_size()

    def remove_video(self, video):
        del self.videos[video.get_identifier]
        self.current_capacity -= video.get_size()

    def has_video(self, video):
        return in self.videos[video.get_identifier()]

    def fits(self, video):
        if video.get_size() + self.current_capacity > self.max_capacity:
            return False
        return True


class Endpoint(object):

    def __init__(self, identifier, latency_to_datacenter):
        self.identifier = identifier
        self.latency_to_datacenter = latency_to_datacenter
        self.close_cache_servers = {}
        self.close_cache_server_latencies = {}
        self.requests = []
        self.cost = 0

    def get_identifier(self):
        return self.identifier

    def latency_to_datacenter(self):
        return self.latency_to_datacenter

    def add_cache_servers(self, cache_server, latency):
        cs_identifier = cache_server.get_identifier()
        self.close_cache_servers[cs_identifier] = cache_server
        self.close_cache_server_latencies[cs_identifier] = latency

    def get_cache_server_latency(self, cache_server):
        return self.close_cache_server_latencies[cache_server.get_identifier()]

    def get_cache_servers(self):
        return self.close_cache_servers

    def has_cache_server(self, cache_server):
        return in self.close_cache_servers[cache_server.get_identifier()]

    def add_request(self, request):
        self.requests.append(request)

    def get_requests(self):
        return self.requests

    def get_cost(self):
        return self.cost


class Video(object):

    def __init__(self, identifier, mb):
        self.identifier = identifier
        self.mb = mb

    def get_identifier(self):
        return self.identifier

    def get_size(self):
        return self.mb


class Request(object):

    def __init__(self, identifier, num_requests, endpoint, video):
        self.identifier = identifier
        self.num_requests = num_requests
        self.endpoint = endpoint
        self.video = video
        self.cache_server = None

    def set_cache_server(self, cache_server):
        self.cache_server = cache_server

    def get_cache_server(self):
        return self.cache_server

    def latency_to_datacenter(self):
        return self.endpoint.latency_to_datacenter()

    def get_video(self):
        return self.video

    def get_identifier(self):
        return self.identifier

    def get_endpoint(self):
        return self.endpoint

    def num_requests(self):
        return self.num_requests

    def get_best_node(self):
        cache_servers = self.endpoint.get_cache_servers()
        min_latency = self.endpoint.latency_to_datacenter()
        best_cache_server = None
        for cs in cache_servers:
            l = self.endpoint.get_cache_server_latency(cs)
            if l < min_latency and cs.fits(self.video):
                min_latency = l
                best_cache_server = cs

        return best_cache_server


num_cache_servers = 0

for r in requests:
    best_cache_server = r.get_best_node()
    if best_cache_server is not None:
        num_cache_servers += 1
        best_cache_server.add_video(r.get_video())
