import random
import os
import numpy as np
import math


def process_file(input_file):
    with open(input_file, 'r') as f:
        first_line = f.readline().split()
        print 'Num videos:', first_line[0]
        print 'Num endpoitns:', first_line[1]
        print 'Num requests:', first_line[2]
        print 'Num of caches:', first_line[3]
        print 'MB:', first_line[4]
        videos = f.readline().split()

        _endpoints = []
        lines = f.readlines()

        for l in xrange(0, len(lines)):
            # latency.append(lines[l].split())
            for l2 in xrange(l, int(first_line[1])):
                _endpoints.append(lines[l+l2].split())
            l += int(first_line[1])

        # for l in xrange(int(first_line[2]), len(lines)):
        #     servers.append(lines[l].split())

    # print len(first_line), len(videos), len(_endpoints)

    return first_line, videos, _endpoints

# class CacheServer(object):
#
#     def __init__(self, identifier, max_capacity):
#         self.max_capacity = max_capacity
#         self.identifier
#         self.videos = {}
#         self.num_videos = 0
#
#     def get_identifier(self):
#         return self.identifier
#
#     def max_capacity(self):
#         return self.max_capacity
#
#     def get_videos(self):
#         return self.videos
#
#     def num_videos(self):
#         return self.num_videos
#
#     def add_video(self, video):
#         self.videos[video.get_identifier()] = video
#
#     def remove_video(self, video):
#         del self.videos[video.get_identifier]
#
#     def has_video(self, video):
#         return in self.videos[video.get_identifier()]
#
#
# class Endpoint(object):
#
#     def __init__(self, identifier, latency_to_datacenter):
#         self.identifier = identifier
#         self.latency_to_datacenter = latency_to_datacenter
#         self.close_cache_servers = {}
#         self.close_cache_server_latencies = {}
#
#     def get_identifier(self):
#         return self.identifier
#
#     def latency_to_datacenter(self):
#         return self.latency_to_datacenter
#
#     def add_cache_servers(self, cache_server, latency):
#         cs_identifier = cache_server.get_identifier()
#         self.close_cache_servers[cs_identifier] = cache_server
#         self.close_cache_server_latencies[cs_identifier] = latency
#
#     def get_cache_server_latency(self, cache_server):
#         return self.close_cache_server_latencies[cache_server.get_identifier()]
#
#     def get_cache_servers(self):
#         return self.close_cache_servers
#
#     def has_cache_server(self, cache_server):
#         return in self.close_cache_servers[cache_server.get_identifier()]
#
#
# class Video(object):
#
#     def __init__(self, identifier, mb):
#         self.identifier = identifier
#         self.mb = mb
#
#     def get_identifier(self):
#         return self.identifier
#
#     def get_size(self):
#         return self.mb
#
#
# class Requests(object):
#
#     def __init__(self, identifier, num_requests, endpoint, video):
#         self.identifier = identifier
#         self.num_requests = num_requests
#         self.endpoint = endpoint
#         self.video = video
#         self.cache_server = None
#
#     def set_cache_server(self, cache_server):
#         self.cache_server = cache_server
#
#     def get_cache_server(self):
#         return self.cache_server
#
#     def latency_to_datacenter(self):
#         cache_server = self.endpoint.get_cache_servers()
#         min_latency = self.endpoint.latency_to_datacenter()
#         for k in cache_server:
#             pass
#
#         return self.endpoint.latency_to_datacenter - self.
#
#     def get_video(self):
#         return self.video
#
#     def get_identifier(self):
#         return self.identifier
#
#     def get_endpoint(self):
#         return self.endpoint
#
#     def num_requests(self):
#         return self.num_requests
#
#
# videos = []
# requests = []
# endpoints = []
# cache_servers = []

if __name__ == '__main__':
    process_file('kittens.bin')