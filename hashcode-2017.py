import random
import os
import numpy as np
import math



def process_file(input_file):
    with open(input_file, 'r') as f:
        # TODO Implement.


class CacheServer(object):

    def __init__(self, identifier, max_capacity):
        self.max_capacity = max_capacity
        self.identifier
        self.videos = {}
        self.num_videos = 0

    def get_identifier(self):
        return self.identifier

    def max_capacity(self):
        return self.max_capacity

    def get_videos(self):
        return self.videos

    def num_videos(self):
        return self.num_videos

    def add_video(self, video):
        self.videos[video.get_identifier()] = video

    def remove_video(self, video):
        del self.videos[video.get_identifier]

    def has_video(self, video):
        return in self.videos[video.get_identifier()]


class Endpoint(object):

    def __init__(self, identifier, latency_to_datacenter):
        self.identifier = identifier
        self.latency_to_datacenter = latency_to_datacenter
        self.close_cache_servers = {}

    def get_identifier(self):
        return self.identifier

    def latency_to_datacenter(self):
        return self.latency_to_datacenter

    def add_cache_servers(self, cache_server):
        self.close_cache_servers[cahce_server.get_identifier()] = cache_server

    def has_cache_server(self, cache_server):
        return in self.close_cache_servers[cache_server.get_identifier()]


class Video(object):

    def __init__(self, identifier, mb):
        self.identifier = identifier
        self.mb = mb

    def get_identifier(self):
        return self.identifier

    def get_size(self):
        return self.mb


class Requests(object):

    def __init__(self, identifier, num_requests, endpoint, video):
        self.identifier = identifier
        self.num_requests = num_requests
        self.endpoint = endpoint
        self.video = video

    def get_video(self):
        return self.video

    def get_identifier(self):
        return self.identifier

    def get_endpoint(self):
        return self.endpoint

    def num_requests(self):
        return self.num_requests
